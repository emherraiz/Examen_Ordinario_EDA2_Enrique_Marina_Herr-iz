def usar_la_fuerza(mochila, objetos_sacados = 0):
    # Caso base: si la mochila está vacía, se retorna una tupla con la información de si se encontró un sable de luz y cuántos objetos se sacaron
    if not mochila:
        return (False, objetos_sacados)
    # Caso recursivo: se saca el último objeto agregado a la mochila y se llama recursivamente a la función con la mochila actualizada
    objeto = mochila.pop()
    if objeto == "sable de luz":
        return (True, objetos_sacados + 1)
    else:
        return usar_la_fuerza(mochila, objetos_sacados + 1)

mochila = ["comunicador", "pistola láser", "sable de luz", "rations"]

encontrado, objetos_sacados = usar_la_fuerza(mochila)

print("Se encontró un sable de luz:", encontrado)
print("Objetos sacados antes de encontrar el sable de luz:", objetos_sacados)
