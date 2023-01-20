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
