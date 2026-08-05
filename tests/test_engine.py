from wordle.engine import evaluar

def test_todas_las_letras_estan_en_posicion_correcta():
    resultado = evaluar("PANDA", "PANDA")
    assert resultado == ["verde", "verde", "verde", "verde", "verde"]

def test_todas_las_letras_estan_ausentes():
    resultado = evaluar("REINA", "PULSO")
    assert resultado == ["gris", "gris", "gris", "gris", "gris"]

def test_identifica_letra_en_posicion_incorrecta():
    resultado = evaluar("DARLE", "PANDA")

    assert resultado == [
        "amarillo",
        "verde",
        "gris", 
        "gris",
        "gris",
    ]
def test_no_marca_repeticiones_que_no_existen_en_la_solucion():
    resultado = evaluar("PERRO", "TEMOR")

    assert resultado == [
        "gris",
        "verde",
        "amarillo",
        "gris",
        "amarillo",
    ]