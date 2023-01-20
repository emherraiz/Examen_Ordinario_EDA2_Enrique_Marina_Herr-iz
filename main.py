from Ejercicio_1_y_2 import stormtrooper
from Ejercicio_3 import artefactosvaliosos
from Ejercicio_4 import usar_la_fuerza
from Ejercicio_5 import ejercicio_5
from Ejercicio_6 import ejercicio_6
from Ejercicio_7 import ejercicio_7
from Ejercicio_8 import ejercicio_8
import pytest

if __name__ == "__main__":
    print('Ejercicio 1 y 2')
    pytest.main(['-v', 'Ejercicio_1_y_2/test_stormtrooper.py'])
    print('Ejercicio 3')
    pytest.main(['-v', 'Ejercicio_3/test_artefactos_valiosos.py'])
    print('Ejercicio 4')
    pytest.main(['-v', 'Ejercicio_4/test_usar_la_fuerza.py'])
    print('Ejercicio 5')
    pytest.main(['-v', 'Ejercicio_5/test_mochila_01.py'])
    print('Ejercicio 6')

