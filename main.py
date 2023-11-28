import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from visualizacion_datos.visualizacion_datos import Grafica, Hilo

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Interfaz para sensor")
        self.mostrar_grafica()
    
    def mostrar_grafica(self):
        self.grafica = Grafica()
        self.setCentralWidget(self.grafica)
        self.hilo = Hilo(self.grafica)
        self.hilo.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())