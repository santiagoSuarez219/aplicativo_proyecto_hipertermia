import time
from PyQt5.QtCore import QThread
from comunicacion_serial.comunicacion_serial import comunicacion_serial
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class ImagenTermica(QThread):
    def __init__(self, grafica):
        super(ImagenTermica, self).__init__() 
        self.grafica = grafica
        self.comunicacion_serial = comunicacion_serial(vid=0x1A86, pid=0x7523, baudrate=115200)
        self.comunicacion_serial.conectar()
        self.data = self.comunicacion_serial.leer()

    def run(self):
        while True:
            self.actualizar_datos()
            time.sleep(.050)

    def actualizar_datos(self):
        self.grafica.g1.clear()
        self.data = self.comunicacion_serial.leer()
        self.grafica.g1.imshow(self.data, cmap='jet')
        self.grafica.draw()

class Grafica(FigureCanvasQTAgg):
    def __init__(self):
        figura = Figure()
        super(Grafica, self).__init__(figura)
        self.g1 = figura.add_subplot(111)