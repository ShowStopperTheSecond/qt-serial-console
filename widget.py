# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

import serial
import serial.tools.list_ports

from PySide6.QtCore import QThread, Signal, QTimer, Qt

# Explicitly import Serial class to avoid attribute errors
from serial import Serial


class SerialThread(QThread):
    data_received = Signal(str)
    error_occurred = Signal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial = None
        self.running = True

    def run(self):
        try:
            # Create serial connection using explicit Serial class
            self.serial = Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=1
            )
            while self.running:
                if self.serial and self.serial.in_waiting:
                    try:
                        data = self.serial.readline().decode('utf-8').strip()
                        if data:
                            self.data_received.emit(data)
                    except UnicodeDecodeError:
                        self.error_occurred.emit("Error: Invalid data encoding")
                    except Exception as e:
                        self.error_occurred.emit(f"Read error: {str(e)}")
        except Exception as e:
            self.error_occurred.emit(f"Connection error: {str(e)}")

    def send_data(self, data):
        if self.serial and self.serial.is_open:
            try:
                self.serial.write((data + '\n').encode('utf-8'))
            except Exception as e:
                self.error_occurred.emit(f"Write error: {str(e)}")

    def stop(self):
        self.running = False
        if self.serial and self.serial.is_open:
            self.serial.close()




class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.serial_thread = None
        self.received_response = None

        self.refresh_ports()

        self.command_history = []
        self.history_index = -1

        self.script_commands = []
        self.current_script_index = 0
        self.script_running = False
        self.script_timer = QTimer()
        self.ui.connect_btn.clicked.connect(self.toggle_connection)
        self.ui.disconnect_btn.clicked.connect(self.toggle_connection)
        self.ui.command_input.returnPressed.connect(self.send_command)
        self.ui.send_command.clicked.connect(self.send_command)
        self.ui.script_progress.setVisible(False)



        self.ui.start_script_btn.clicked.connect(self.start_script_execution)

        self.ui.stop_script_btn.clicked.connect(self.stop_script_execution)
        self.ui.stop_script_btn.setEnabled(False)
        self.ui.clear_script_btn.clicked.connect(self.clear_script)
        self.ui.load_file_btn.clicked.connect(self.load_script_from_file)
        self.ui.save_file_btn.clicked.connect(self.save_script_to_file)
        self.script_timer.timeout.connect(self.send_next_script_command)
        self.ui.command_input.installEventFilter(self)

    def eventFilter(self, obj, event):
        # Handle up/down arrows for command history
        if obj is self.ui.command_input and event.type() == event.Type.KeyPress:
            if event.key() == Qt.Key.Key_Up:
                self.show_prev_command()
                return True
            elif event.key() == Qt.Key.Key_Down:
                self.show_next_command()
                return True
        return super().eventFilter(obj, event)

    def get_color(self, name):
        return {
            "red": "#FF0000",
            "green": "#006400",
            "blue": "#0000FF",
            "black": "#000000",
            "orange": "#FF8C00"
        }.get(name, "#000000")

    def refresh_ports(self):
            self.ui.port_combo.clear()
            try:
                ports = serial.tools.list_ports.comports()
                for port in sorted(ports):
                    self.ui.port_combo.addItem(port.device)
            except Exception as e:
                self.append_output(f"Port scan error: {str(e)}", "red")

    def toggle_connection(self):
        if self.ui.connect_btn.isEnabled():
            # Connect
            port = self.ui.port_combo.currentText()
            baud = int(self.ui.baud_combo.currentText())

            if not port:
                QMessageBox.critical(self, "Error", "No port selected!")
                return

            try:
                self.serial_thread = SerialThread(port, baud)
                self.serial_thread.data_received.connect(self.handle_received_data)
                self.serial_thread.error_occurred.connect(self.handle_error)
                self.serial_thread.start()

                self.ui.connect_btn.setEnabled(False)
                self.ui.disconnect_btn.setEnabled(True)
                self.ui.port_combo.setEnabled(False)
                self.ui.baud_combo.setEnabled(False)
                self.ui.refresh_btn.setEnabled(False)
                self.append_output(f"Connected to {port} @ {baud} baud")

            except Exception as e:
                QMessageBox.critical(self, "Connection Error", str(e))
        else:
            # Disconnect
            if self.serial_thread:
                self.serial_thread.stop()
                self.serial_thread.quit()
                self.serial_thread.wait()
                self.serial_thread = None

            self.ui.connect_btn.setEnabled(True)
            self.ui.disconnect_btn.setEnabled(False)
            self.ui.port_combo.setEnabled(True)
            self.ui.baud_combo.setEnabled(True)
            self.ui.refresh_btn.setEnabled(True)
            self.append_output("Disconnected")

    def handle_received_data(self, data):
        self.append_output(f"<< {data}", "green")
        self.received_response = True

    def handle_error(self, error):
        self.append_output(error, "red")

    def append_output(self, text, color=None):
        if color:
            self.ui.terminal_output.setTextColor(self.get_color(color))
        self.ui.terminal_output.append(text)
        self.ui.terminal_output.setTextColor(self.get_color("black"))  # Reset color

    def send_command(self):
        if not self.serial_thread or not self.serial_thread.isRunning():
            QMessageBox.warning(self, "Not Connected", "Not connected to any port!")
            return

        command = self.ui.command_input.text().strip()
        if not command:
            return

        try:
            # Add to history
            self.command_history.append(command)
            self.history_index = -1

            # Send command
            self.serial_thread.send_data(command)
            self.append_output(f">> {command}", "blue")
            self.ui.command_input.clear()
        except Exception as e:
            self.append_output(f"Error: {str(e)}", "red")
        self.received_response = False
    def eventFilter(self, obj, event):
        # Handle up/down arrows for command history
        if obj is self.ui.command_input and event.type() == event.Type.KeyPress:
            if event.key() == Qt.Key.Key_Up:
                self.show_prev_command()
                return True
            elif event.key() == Qt.Key.Key_Down:
                self.show_next_command()
                return True
    def closeEvent(self, event):
        if self.serial_thread and self.serial_thread.isRunning():
            self.serial_thread.stop()
            self.serial_thread.quit()
            self.serial_thread.wait()
        event.accept()

    def show_prev_command(self):
        if self.command_history:
            if self.history_index < len(self.command_history) - 1:
                self.history_index += 1
            self.ui.command_input.setText(self.command_history[-self.history_index - 1])

    def show_next_command(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.ui.command_input.setText(self.command_history[-self.history_index - 1])
        else:
            self.history_index = -1
            self.ui.command_input.clear()

        return super().eventFilter(obj, event)

    def load_script_from_file(self):
            file_path, _ = QFileDialog.getOpenFileName(
                self, "Open Command Script", "", "Text Files (*.txt);;All Files (*)"
            )
            if file_path:
                try:
                    with open(file_path, 'r') as file:
                        commands = file.read()
                        self.ui.script_input.setPlainText(commands)
                        self.append_output(f"Loaded script from: {file_path}", "green")
                except Exception as e:
                    self.append_output(f"Error loading script: {str(e)}", "red")

    def save_script_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Command Script", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.ui.script_input.toPlainText())
                    self.append_output(f"Script saved to: {file_path}", "green")
            except Exception as e:
                self.append_output(f"Error saving script: {str(e)}", "red")

    def clear_script(self):
        self.ui.script_input.clear()
        self.append_output("Script cleared", "orange")

    def start_script_execution(self):
        if not self.serial_thread or not self.serial_thread.isRunning():
            QMessageBox.warning(self, "Not Connected", "Not connected to any port!")
            return

        # Get commands from text area
        script_text = self.ui.script_input.toPlainText().strip()
        if not script_text:
            QMessageBox.warning(self, "Empty Script", "No commands in the script area!")
            return

        # Split into commands and filter empty lines
        self.script_commands = [cmd.strip() for cmd in script_text.split('\n') if cmd.strip()]
        self.current_script_index = 0

        if not self.script_commands:
            QMessageBox.warning(self, "Empty Script", "No valid commands found!")
            return

        # Setup UI for script execution
        self.script_running = True
        self.ui.start_script_btn.setEnabled(False)
        self.ui.stop_script_btn.setEnabled(True)
        self.ui.clear_script_btn.setEnabled(False)
        self.ui.load_file_btn.setEnabled(False)
        self.ui.save_file_btn.setEnabled(False)

        # Setup progress bar
        self.ui.script_progress.setVisible(True)
        self.ui.script_progress.setRange(0, len(self.script_commands))
        self.ui.script_progress.setValue(0)

        self.append_output("Starting script execution...", "orange")

        # Get delay between commands
        delay_ms = int(self.ui.delay_combo.currentText())

        # Start sending commands with specified delay
        self.script_timer.start(delay_ms)
        self.send_next_script_command()

    def send_next_script_command(self):
        if not self.script_running or self.current_script_index >= len(self.script_commands) :
            self.stop_script_execution()
            return
        if not  self.received_response:
            return

        command = self.script_commands[self.current_script_index]

        try:
            # Send command
            self.serial_thread.send_data(command)
            self.append_output(f">> [SCRIPT] {command}", "blue")

            # Update progress
            self.current_script_index += 1
            self.ui.script_progress.setValue(self.current_script_index)

            # Check if we've finished
            if self.current_script_index >= len(self.script_commands):
                self.stop_script_execution()
                self.append_output("Script execution completed", "green")
        except Exception as e:
            self.append_output(f"Script error: {str(e)}", "red")
            self.stop_script_execution()
        self.received_response = False

    def stop_script_execution(self):
        self.script_running = False
        self.script_timer.stop()

        # Restore UI
        self.ui.start_script_btn.setEnabled(True)
        self.ui.stop_script_btn.setEnabled(False)
        self.ui.clear_script_btn.setEnabled(True)
        self.ui.load_file_btn.setEnabled(True)
        self.ui.save_file_btn.setEnabled(True)

        if self.current_script_index < len(self.script_commands):
            self.append_output("Script execution stopped", "orange")
            self.ui.script_progress.setValue(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
