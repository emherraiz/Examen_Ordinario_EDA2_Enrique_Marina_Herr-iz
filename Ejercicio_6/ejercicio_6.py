import random
class StormtrooperManager:
    def __init__(self):
        self.legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
        self.tabla_hash1 = {}
        self.tabla_hash2 = {}

    def generar_stormtroopers(self):
        self.stormtroopers = []
        for i in range(2000):
            legión = random.choice(self.legiones)
            codigo = legión + '-'
            for j in range(4):
                codigo += str(random.randint(0, 9))
            stormtrooper = stormtrooper.Stormtrooper(codigo)
            self.stormtroopers.append(stormtrooper)

    def cargar_stormtroopers(self):
        for stormtrooper in self.stormtroopers:
            ultimos_digitos = stormtrooper.codigo[-3:]
            if ultimos_digitos not in self.tabla_hash1:
                self.tabla_hash1[ultimos_digitos] = []
            self.tabla_hash1[ultimos_digitos].append(stormtrooper)

            inicial_legion = stormtrooper.codigo[:2]
            if inicial_legion not in self.tabla_hash2:
                self.tabla_hash2[inicial_legion] = []
            self.tabla_hash2[inicial_legion].append(stormtrooper)

    def eliminar_stormtrooper(self, codigo):
        for stormtrooper in self.stormtroopers:
            if stormtrooper.codigo == codigo:
                ultimos_digitos = stormtrooper.codigo[-3:]
                self.tabla_hash1[ultimos_digitos].remove(stormtrooper)
                inicial_legion = stormtrooper.codigo[:2]
                self.tabla_hash2[inicial_legion].remove(stormtrooper)
                self.stormtroopers.remove(stormtrooper)
                return True
        return False

    def obtener_stormtroopers_por_digitos(self, digitos):
        if digitos in self.tabla_hash1:
            return self.tabla_hash1[digitos]
        else:
            return []

    def obtener_stormtroopers_por_legion(self, legion):
        if legion in self.tabla_hash2:
            return self.tabla_hash2[legion]
        else:
            return []

    def asignar_mision(self, digitos, mision):
        stormtroopers_digitos = self.obtener_stormtroopers_por_digitos(digitos)
        for stormtrooper in stormtroopers_digitos:
            stormtrooper.asignar_mision(mision)

