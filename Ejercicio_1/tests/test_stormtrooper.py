from Ejercicio_1 import Stormtrooper
import pytest
def test_calificacion():
    # Create a Stormtrooper object
    nombre = 'AB-1234'
    stormtrooper = Stormtrooper(nombre, 'Soldado')

    # Test the calificacion method
    stormtrooper.calificacion()
    assert stormtrooper.codigo == 'AB'
    assert stormtrooper.cohorte == '1'
