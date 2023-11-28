import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QComboBox, QLabel
from PyQt5.QtCore import Qt
from comunicacion_serial import comunicacion_serial
from comunicacion_mqtt import comunicacion_mqtt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz para sensor")
        self.setGeometry(100, 100, 400, 200)

        self.comunicacion_serial = comunicacion_serial(vid=0x1A86, pid=0x7523, baudrate=115200)
        self.conexion_serial = self.comunicacion_serial.conectar()

        if(not self.conexion_serial):
            self.comunicacion_mqtt = comunicacion_mqtt(broker=" 192.168.1.103", port=1883)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())