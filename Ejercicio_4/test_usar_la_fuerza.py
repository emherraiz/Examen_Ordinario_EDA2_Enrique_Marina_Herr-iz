import pytest
from usar_la_fuerza import usar_la_fuerza

def test_usar_la_fuerza():
    mochila = ["comunicador", "pistola láser", "sable de luz", "rations"]
    encontrado, objetos_sacados = usar_la_fuerza(mochila)
    assert encontrado == True
    assert objetos_sacados == 2
    
    mochila = ["comunicador", "pistola láser", "rations"]
    encontrado, objetos_sacados = usar_la_fuerza(mochila)
    assert encontrado == False
    assert objetos_sacados == 3
    
    mochila = []
    encontrado, objetos_sacados = usar_la_fuerza(mochila)
    assert encontrado == False
    assert objetos_sacados == 0
