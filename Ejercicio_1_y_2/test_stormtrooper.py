import pytest
from stormtrooper import Stormtrooper, experimentacion

def test_stormtrooper_init():
    st = Stormtrooper("ST-1234", "Soldado")
    assert st.nombre == "ST-1234"
    assert st.rango == "Soldado"

def test_stormtrooper_calificacion():
    st = Stormtrooper("ST-1234", "Soldado")
    st.calificacion()
    assert st.codigo == "ST"
    assert st.cohorte == "1"
    assert st.siglo == "2"
    assert st.escuadra == "3"
    assert st.numero == "4"

def test_experimentacion():
    lista_stormtrooper = experimentacion(5)
    assert len(lista_stormtrooper) == 5
    for st in lista_stormtrooper:
        assert isinstance(st, Stormtrooper)
