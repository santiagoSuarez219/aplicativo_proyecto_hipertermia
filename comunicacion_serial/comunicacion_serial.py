import serial
from serial.tools import list_ports

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