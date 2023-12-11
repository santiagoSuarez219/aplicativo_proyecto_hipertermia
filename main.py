import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QFrame, QHBoxLayout, QPushButton
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
        contenedor.setLayout(self.vlyt)
        self.setCentralWidget(contenedor)
    
    def display_widgets(self):
        label = QLabel(self)
        label.setText("Proyecto Hipertermia")
        label.setFont(QFont("Arial", 20, QFont.Bold))
        label.resize(800, 50)
        label.setAlignment(Qt.AlignCenter)

        self.vlyt = QVBoxLayout()
        self.vlyt.addWidget(label)

        self.grafica = Grafica()
        self.imagen_termica = ImagenTermica(self.grafica)   
        self.imagen_termica.start()

        self.vlyt.addWidget(self.grafica)

        self.label_temperatura_maxima = QLabel(self)
        self.label_temperatura_minima = QLabel(self)
        self.label_temperatura_promedio = QLabel(self)

        self.label_temperatura_maxima.setFont(QFont("Arial", 10))
        self.label_temperatura_minima.setFont(QFont("Arial", 10))
        self.label_temperatura_promedio.setFont(QFont("Arial", 10))

        boton_guardar = QPushButton("Guardar")
        boton_guardar.setFont(QFont("Arial", 10))
        
        xlyt = QHBoxLayout()
        xlyt.addWidget(self.label_temperatura_maxima)
        xlyt.addWidget(self.label_temperatura_minima)
        xlyt.addWidget(self.label_temperatura_promedio)
        xlyt.addWidget(boton_guardar)

        self.vlyt.addLayout(xlyt)
        self.imagen_termica.actualizar_labels_signal.connect(self.actualizar_labels_temperatura)
    
    def actualizar_labels_temperatura(self, maxima, minima, promedio):
        self.label_temperatura_maxima.setText(f"Temperatura máxima: {maxima:.2f} °C")
        self.label_temperatura_minima.setText(f"Temperatura mínima: {minima:.2f} °C")
        self.label_temperatura_promedio.setText(f"Temperatura promedio: {promedio:.2f} °C")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())