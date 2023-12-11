import time
from PyQt5.QtCore import QThread, pyqtSignal
from comunicacion_serial.comunicacion_serial import comunicacion_serial
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np

class ImagenTermica(QThread):
    actualizar_labels_signal = pyqtSignal(float, float, float)
    def __init__(self, grafica):
        super(ImagenTermica, self).__init__() 
        self.grafica = grafica
        self.comunicacion_serial = comunicacion_serial(vid=0x1A86, pid=0x7523, baudrate=115200)
        self.comunicacion_serial.conectar()
        self.data_imagen_termica = self.comunicacion_serial.leer()
        self.data_maxima_temperatura = []

    def run(self):
        while True:
            self.actualizar_datos()
            time.sleep(.050)

    def actualizar_datos(self):
        self.data_imagen_termica = self.comunicacion_serial.leer()
        if len(self.data_maxima_temperatura) == 50:
            self.data_maxima_temperatura.pop(0)
        maxima = np.max(self.data_imagen_termica)
        self.data_maxima_temperatura.append(maxima)
        self.grafica.actualizar_graficas(self.data_imagen_termica, self.data_maxima_temperatura)
        
        minima = np.min(self.data_imagen_termica)
        promedio = np.mean(self.data_imagen_termica)
        self.actualizar_labels_signal.emit(maxima, minima, promedio)

class Grafica(FigureCanvasQTAgg):
    def __init__(self):
        figura = Figure()
        super(Grafica, self).__init__(figura)
        self.g1 = figura.add_subplot(121)
        self.g2 = figura.add_subplot(122)
        self.g2.grid(True)
    
    def actualizar_graficas(self, data_g1, data_g2):
        self.g1.clear()
        self.g1.imshow(data_g1, cmap='jet')
        self.g2.clear()
        self.g2.plot(data_g2, '-o')
        self.draw()