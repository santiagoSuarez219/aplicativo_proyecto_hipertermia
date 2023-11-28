import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from comunicacion_serial.comunicacion_serial import comunicacion_serial
from comunicacion_mqtt.comunicacion_mqtt import comunicacion_mqtt

class Hilo(QThread):
    def __init__(self):
        super(Hilo, self).__init__()
    def run(self):
        pass

class grafica(FigureCanvasQTAgg):
    def __init__(self):
        figura = Figure()
        super(grafica, self).__init__(figura)
        
        self.g1 = figura.add_subplot(111)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Interfaz para sensor")
        self.comunicacion_serial = comunicacion_serial(vid=0x1A86, pid=0x7523, baudrate=115200)
        self.comunicacion_serial.conectar()
        self.mostrar_grafica()

        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_datos)
        self.timer.start(100)

        # self.conexion_serial = self.comunicacion_serial.conectar()

        # if(not self.conexion_serial):
        #     self.comunicacion_mqtt = comunicacion_mqtt(broker=" 192.168.1.103", port=1883)
    
    def mostrar_grafica(self):
        self.grafica = grafica()
        self.setCentralWidget(self.grafica)
        self.data = self.comunicacion_serial.leer()

    def actualizar_datos(self):
        self.grafica.g1.clear()
        self.data = self.comunicacion_serial.leer()
        self.grafica.g1.imshow(self.data, cmap='jet')
        self.grafica.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())