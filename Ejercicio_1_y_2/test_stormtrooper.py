import string, random
import pytest
from main import Stormtrooper, experimentacion

def test_experimentacion():
    n = 10
    lista_stormtrooper = experimentacion(n)
    assert len(lista_stormtrooper) == n
    for i in lista_stormtrooper:
        assert isinstance(i, Stormtrooper)


def test_nombre_stormtrooper_valido():
    nombres_stormtroopers = [stormtrooper.nombre for stormtrooper in experimentacion(5)]
    for nombre in nombres_stormtroopers:
        assert nombre[2] == '-'
        assert nombre[:2].isalpha() and nombre[:2].isupper()
        assert nombre[3:].isnumeric()
        assert len(nombre) == 7
