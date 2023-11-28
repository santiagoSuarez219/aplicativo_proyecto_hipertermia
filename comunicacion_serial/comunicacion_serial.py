import serial
from serial.tools import list_ports
import json
import numpy as np

class comunicacion_serial():
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
        try:
            self.conexion = serial.Serial(self.puerto, self.baudrate)
            print("Conexión establecida con el sensor")
            return True
        except:
            print("Error al conectar con el sensor")
            return False

    def leer(self):
        try: 
            data = self.conexion.readline().decode('utf-8').strip().split(",")
            data.pop()
            data = np.array(data, dtype=float).reshape(24, 32)
            return data
        except:
            print("Error al leer y decodificar JSON")

if __name__ == "__main__":
    print("Iniciando comunicación serial")
    comunicacion_serial = comunicacion_serial(vid=0x1A86, pid=0x7523, baudrate=115200)
    if(comunicacion_serial.conectar()):
        contador = 0
        while contador < 10:
            comunicacion_serial.leer()
            contador += 1