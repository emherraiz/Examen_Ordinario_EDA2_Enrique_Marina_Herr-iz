import string, random
class stormtrooper():
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print('Stormtrooper se ha creado con éxito')
        self.calificacion()

    def calificacion(self):
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


        lista_stormtrooper.append(stormtrooper(nombre, 'Soldado'))

    for i in lista_stormtrooper:
        print(i)

    return lista_stormtrooper

a = experimentacion(10)
