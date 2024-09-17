print("Clases version 2 el constructor")
class Perro:
    # Funcion constructor 
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad
    # Funciones creadas por el usuario
    def morder(self):
        print("Chale el perro me mordio")
    def chatperro(self, mensaje):
        print(f"Chat perro: {mensaje}")
    def chatperra(self, mensajep):
        print(f"Chat perra: {mensajep}")
    def datos(self):
        print(f"Color {self.color} edad {self.edad}")
# Crear el objeto
chihuas=Perro("pinto",2)
# llamas a funciones
chihuas.datos()
chihuas.morder()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola boby")
chihuas.chatperro("Quieres ser mi gugguu?")
chihuas.chatperra("grrru......")