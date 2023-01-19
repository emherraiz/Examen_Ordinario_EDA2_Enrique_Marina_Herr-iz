class ArtefactosValiosos:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        print("La conserva ha sido creada con éxito.")

    def str(self):
        return "Información de la conserva: peso={}, nombre={}, precio={}, fecha de caducidad={}".format(self.peso, self.nombre, self.precio, self.fecha_caducidad)


artefacto1 = ArtefactosValiosos(1, "Conserva de tomate", 2.5, "2022-12-31")
artefacto2 = ArtefactosValiosos(2, "Conserva de pimientos", 3.0, "2022-11-30")
artefacto3 = ArtefactosValiosos(3, "Conserva de alcachofas", 4.5, "2022-10-31")
artefactos_valiosos = [artefacto1, artefacto2, artefacto3]

# Mostrar los datos de los artefactos valiosos ordenados por fecha de caducidad
artefactos_valiosos.sort(key=lambda x: x.fecha_caducidad)
for artefacto in artefactos_valiosos:
    print(artefacto)

# Modificar el precio de un artefacto valioso
artefacto1.precio = 2.0
print("El nuevo precio de la conserva de tomate es: ",artefacto1.precio)
