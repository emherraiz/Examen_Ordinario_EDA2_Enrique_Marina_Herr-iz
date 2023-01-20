import pytest
from ejercicio_6 import StormtrooperManager

def test_StormtrooperManager_generar_stormtroopers():
    manager = StormtrooperManager()
    manager.generar_stormtroopers()
    assert len(manager.stormtroopers) == 2000

def test_StormtrooperManager_cargar_stormtroopers():
    manager = StormtrooperManager()
    manager.generar_stormtroopers()
    manager.cargar_stormtroopers()
    assert len(manager.tabla_hash1) > 0
    assert len(manager.tabla_hash2) > 0

def test_StormtrooperManager_eliminar_stormtrooper():
    manager = StormtrooperManager()
    manager.generar_stormtroopers()
    manager.cargar_stormtroopers()
    codigo = manager.stormtroopers[0].codigo
    assert manager.eliminar_stormtrooper(codigo) == True
    assert manager.eliminar_stormtrooper(codigo) == False

def test_StormtrooperManager_obtener_stormtroopers_por_digitos():
    manager = StormtrooperManager()
    manager.generar_stormtroopers()
    manager.cargar_stormtroopers()
    digitos = manager.stormtroopers[0].codigo[-3:]
    assert len(manager.obtener_stormtroopers_por_digitos(digitos)) > 0
    assert len(manager.obtener_stormtroopers_por_digitos("000")) == 0

def test_StormtrooperManager_obtener_stormtroopers_por_digitos(self):
    stormtrooper_manager = StormtrooperManager()
    stormtrooper_manager.generar_stormtroopers()
    stormtrooper_manager.cargar_stormtroopers()
    stormtroopers_digitos = stormtrooper_manager.obtener_stormtroopers_por_digitos("001")
    assert len(stormtroopers_digitos) > 0
    for stormtrooper in stormtroopers_digitos:
        assert stormtrooper.codigo[-3:] == "001"

def test_StormtrooperManager_obtener_stormtroopers_por_legion(self):
    stormtrooper_manager = StormtrooperManager()
    stormtrooper_manager.generar_stormtroopers()
    stormtrooper_manager.cargar_stormtroopers()
    stormtroopers_legion = stormtrooper_manager.obtener_stormtroopers_por_legion("FL")
    assert len(stormtroopers_legion) > 0
    for stormtrooper in stormtroopers_legion:
        assert stormtrooper.codigo[:2] == "FL"

def test_StormtrooperManager_asignar_mision(self):
    stormtrooper_manager = StormtrooperManager()
    stormtrooper_manager.generar_stormtroopers()
    stormtrooper_manager.cargar_stormtroopers()
    stormtrooper_manager.asignar_mision("001", "Mision 1")
    stormtroopers_digitos = stormtrooper_manager.obtener_stormtroopers_por_digittos("123")

    assert len(stormtroopers_digitos) == 2
    assert stormtroopers_digitos[0].codigo == "FL-1234"
    assert stormtroopers_digitos[1].codigo == "TF-5123"

def test_StormtrooperManager_asignar_mision():
    stormtrooper_manager = StormtrooperManager()
    stormtrooper_manager.generar_stormtroopers()
    stormtrooper_manager.cargar_stormtroopers()
    stormtrooper_manager.asignar_mision("123", "Misión en Tatooine")
    stormtroopers_digitos = stormtrooper_manager.obtener_stormtroopers_por_digitos("123")
    for stormtrooper in stormtroopers_digitos:
        assert stormtrooper.mision == "Misión en Tatooine"


def test_StormtrooperManager_eliminar_stormtrooper():
    stormtrooper_manager = StormtrooperManager()
    stormtrooper_manager.generar_stormtroopers()
    stormtrooper_manager.cargar_stormtroopers()
    assert stormtrooper_manager.eliminar_stormtrooper("FL-1234") == True
    assert stormtrooper_manager.eliminar_stormtrooper("FL-1234") == False
    stormtroopers_digitos = stormtrooper_manager.obtener_stormtroopers_por_digitos("123")
    assert len(stormtroopers_digitos) == 1
    assert stormtroopers_digitos[0].codigo == "TF-1234"
    assert stormtroopers_digitos[1].código == "FL-1234"
    assert len(stormtroopers_digitos) == 2

def test_StormtrooperManager_asignar_mision():
    stormtrooper_manager = StormtrooperManager()
    stormtrooper_manager.generar_stormtroopers()
    stormtrooper_manager.cargar_stormtroopers()
    stormtrooper_manager.asignar_mision("234", "Misión X")
    stormtroopers_digitos = stormtrooper_manager.obtener_stormtroopers_por_digitos("234")
    assert stormtroopers_digitos[0].mision == "Misión X"
    assert stormtroopers_digitos[1].mision == "Misión X"
    assert len(stormtroopers_digitos) == 2
