import kivy
kivy.require("2.0.0")  # Asegúrate de tener al menos esta versión instalada

from kivy.app import App
from kivy.uix.label import Label

class MiPrimeraApp(App):
    def build(self):
        return Label(text="¡Hola, Kivy!",font_size=150)

if __name__ == '__main__':
    MiPrimeraApp().run()
