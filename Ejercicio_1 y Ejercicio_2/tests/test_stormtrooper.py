import pytest
'''
def test_calificacion():
    # Create a Stormtrooper object
    nombre = 'AB-1234'
    stormtrooper = stormtrooper.Stormtrooper(nombre, 'Soldado')

    # Test the calificacion method
    stormtrooper.calificacion()
    assert stormtrooper.codigo == 'AB'
    assert stormtrooper.cohorte == '1'oooo
'''

def test_experimentacion():
    stormtroopers = stormtrooper.experimentacion(3)
    assert len(stormtroopers) == 3
    for stormtrooper in stormtroopers:
        assert isinstance(stormtrooper, stormtrooper.Stormtrooper)
        assert '-' in stormtrooper.nombre
        assert len(stormtrooper.nombre) == 6
        assert stormtrooper.rango == 'Soldado'