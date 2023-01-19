def test_crear_artefactos():
    artefacto1 = artefactosvaliosos.ArtefactosValiosos(1, "Conserva de tomate", 2.5, "2022-12-31")
    artefacto2 = artefactosvaliosos.ArtefactosValiosos(2, "Conserva de pimientos", 3.0, "2022-11-30")
    artefacto3 = artefactosvaliosos.ArtefactosValiosos(3, "Conserva de alcachofas", 4.5, "2022-10-31")
    assert artefacto1.nombre == "Conserva de tomate"
    assert artefacto2.nombre == "Conserva de pimientos"
    assert artefacto3.nombre == "Conserva de alcachofas"

def test_orden_artefactos():
    artefacto1 = artefactosvaliosos.ArtefactosValiosos(1, "Conserva de tomate", 2.5, "2022-12-31")
    artefacto2 = artefactosvaliosos.ArtefactosValiosos(2, "Conserva de pimientos", 3.0, "2022-11-30")
    artefacto3 = artefactosvaliosos.ArtefactosValiosos(3, "Conserva de alcachofas", 4.5, "2022-10-31")
    artefactos_valiosos = [artefacto1, artefacto2, artefacto3]
    artefactos_valiosos.sort(key=lambda x: x.fecha_caducidad)
    assert artefactos_valiosos[0].fecha_caducidad == '2022-10-31'
    assert artefactos_valiosos[1].fecha_caducidad == '2022-11-30'
    assert artefactos_valiosos[2].fecha_caducidad == '2022-12-31'

def test_modificar_precio():
    artefacto1 = artefactosvaliosos.ArtefactosValiosos(1, "Conserva de tomate", 2.5, "2022-12-31")
    artefacto1.precio = 2.0
    assert artefacto1.precio == 2.0
