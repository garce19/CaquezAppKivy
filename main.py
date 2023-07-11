import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        return Label(text='Hola a todos')

if __name__ == '__main__':
    MainApp().run()