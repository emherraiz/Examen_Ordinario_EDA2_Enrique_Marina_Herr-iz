import string, random
class Nombre:
    def __init__(self, nombre):
        self.nombre = nombre

class Rango:
    def __init__(self, rango):
        self.rango = rango
class Stormtrooper(Nombre, Rango):
    def __init__(self, nombre, rango):
        # super().__init__(nombre)
        # super().__init__(rango)
        self.nombre = nombre
        self.rango = rango
        print(f'Stormtrooper {self.nombre} se ha creado con éxito')
        self.calificacion()

    def calificacion(self):
        if '-' not in self.nombre:
            self.codigo = self.nombre[0:2]
            self.cohorte = self.nombre[2]
            self.siglo = self.nombre[3]
            self.escuadra = self.nombre[4]
            self.numero = self.nombre[5]

        else:
            temp = self.nombre.split('-')
            self.codigo = temp[0]
            temp = temp[1]
            self.cohorte = temp[0]
            self.siglo = temp[1]
            self.escuadra = temp[2]
            self.numero = temp[3]

    def __str__(self):
        return '\nNombre: ' + self.nombre + '\nRango: ' + self.rango + '\nCodigo: ' + self.codigo + '\nCohorte: ' + self.cohorte + '\nSiglo: ' + self.siglo + '\nEscuadra: ' + self.escuadra + '\nNumero: ' + self.numero

def experimentacion(n):
    lista_stormtrooper = []
    for i in range(n):
        nombre = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + '-'
        for j in range(4):
            nombre += str(random.randint(0,9))


        lista_stormtrooper.append(Stormtrooper(nombre, 'Soldado'))

    for i in lista_stormtrooper:
        print(i)

    return lista_stormtrooper

a = experimentacion(5)
