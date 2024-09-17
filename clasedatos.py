class Informacion:
    def mi_lista(self):
        lista_Nomperros = ["boby","Dollar","Fany"]
        for x in lista_Nomperros:
            print(x)
    def mi_conjunto(self):
        conjunto_colores = {"Rojo", "Azul", "Naranja"}
        for x in conjunto_colores:
            print(x)
    def mi_tupla(self):
        tupla_frutas = ("Manzana", "Kiwi", "Moras")
        for x in tupla_frutas:
            print(x)
    def mi_Dic(self):
        dicc_Alumno = {
        "Nombre": "Cristian Eduardo ",
        "Nac": 2007,
        "Salon": 29}
        for x in dicc_Alumno:
            print(x)
# creando el objeto
datos=Informacion()
print("Listado de nombre de perros")
datos.mi_lista()
print("Conjunto de colores")
datos.mi_conjunto()
print("Tupla de Frutas")
datos.mi_tupla()
print("Diccionario de alumno")
datos.mi_Dic()