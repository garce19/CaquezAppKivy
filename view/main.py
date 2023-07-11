import kivy
kivy.require('2.2.1')

from model.Usuario import Usuario
from controller.UsuarioController import UsuarioController
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        return Label(text='CaquezApp')

usuario1 = Usuario()
usuarioController = Usuario
print(usuario1)

'1003739462', 'Germán Alberto', 'Rojas Cetina', 'garcejr@gmail.com', '3164145899', 'Santa Bárbara', 'Avenida 4 #1-33'

if __name__ == '__main__':
    MainApp().run()