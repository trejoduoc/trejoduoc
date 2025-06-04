from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

# Creamos la aplicación
app = QApplication(sys.argv)

# Creamos la ventana principal
ventana = QWidget()
ventana.setWindowTitle("Mi primera app con PySide6")
ventana.setGeometry(100, 100, 300, 200)  # x, y, ancho, alto

# Creamos un layout y un label
layout = QVBoxLayout()
label = QLabel("¡Hola, mundo!")
layout.addWidget(label)

# Aplicamos el layout a la ventana
ventana.setLayout(layout)

# Mostramos la ventana
ventana.show()

# Ejecutamos el loop de la app
sys.exit(app.exec())
