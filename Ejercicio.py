class stormtrooper():
    def __init__(self, nombre, rango):
        self.name = nombre
        self.rango = rango
        print('Stormtrooper se ha creado con éxito')

    def calificacion(self, nombre):
        temp = nombre.split('-')
        self.codigo = temp[0]
        temp = temp[1].split()
        self.cohoerte = temp[0]
        self.siglo = temp[1]
        self.escuadra = temp[2]
        self.numero = temp[3]

    def __str__(self):
        return 'Nombre: ' + self.name
