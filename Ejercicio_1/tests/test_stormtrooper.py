
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

def test_stormtrooper_calificacion():
    stormtrooper = stormtrooper.Stormtrooper("TK-8654", "Capitán")
    assert stormtrooper.calificacion() == "Codigo de legion: TK, Identificador de cohorte: 8, Identificador de siglo: 6, Identificador de escuadra: 5, Numero de trooper: 4"

if __name__ == "main":
    import pytest
    pytest.main()
