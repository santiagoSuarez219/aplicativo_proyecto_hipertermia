import serial
from serial.tools import list_ports
import time

class ComunicacionSerial():
    def __init__(self, vid, pid, baudrate):
        self.vid = vid
        self.pid = pid
        self.puerto = None
        self.baudrate = baudrate
        self.conexion = None

    def encontrar_puerto_sensor(self):
        puertos_disponibles = list_ports.comports()
        for puerto in puertos_disponibles:
            if puerto.vid == self.vid and puerto.pid == self.pid:
                self.puerto = puerto.device
                print("Puerto encontrado: ", self.puerto)

    def conectar(self):
        self.encontrar_puerto_sensor()
        if self.puerto:
            self.conexion = serial.Serial(self.puerto, self.baudrate)
            print("Conexión establecida con el sensor")
            return self.conexion
        else:
            return None
    
    

