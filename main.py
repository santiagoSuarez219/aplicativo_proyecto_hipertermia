import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QFrame, QHBoxLayout, QWidget, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from visualizacion_datos.visualizacion_datos import Grafica, ImagenTermica

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Interfaz grafica")
        self.setGeometry(200, 200, 1300, 500)
        self.display_widgets()
        contenedor = QFrame()
        contenedor.setLayout(self.glyt_principal)
        self.setCentralWidget(contenedor)
    
    def display_widgets(self):
        label = QLabel(self)
        label.setText("Proyecto Hipertermia")
        label.setFont(QFont("Arial", 20, QFont.Bold))
        label.resize(800, 50)
        label.setAlignment(Qt.AlignCenter)

        self.glyt_principal = QGridLayout(self)
        self.glyt_principal.addWidget(label, 0, 0, 1, 2)

        self.grafica = Grafica()
        self.imagen_termica = ImagenTermica(self.grafica)   
        self.imagen_termica.start()

        self.glyt_principal.addWidget(self.grafica, 1, 0, 1, 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())