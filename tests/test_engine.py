import pytest
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

def test_acepta_mayusculas_y_minusculas():
    resultado = evaluar("panda", "PANDA")

    assert resultado == ["verde"] * 5

@pytest.mark.parametrize(
    ("intento", "solucion"),
    [
        ("CASA", "PANDA"),
        ("PANDA", "CASA"),
        ("PANDAS", "PANDA"),
        ("PANDA", "PANDAS"),
    ],
)
def test_rechaza_palabras_con_longitud_invalida(intento, solucion):
    with pytest.raises(ValueError, match="cinco letras"):
        evaluar(intento, solucion)

def test_ignora_tildes_en_las_vocales():
    resultado = evaluar("ÁRBOL", "ARBOL")

    assert resultado == ["verde"] * 5

def test_distingue_ene_de_enie():
    resultado = evaluar("CANON", "CAÑON")

    assert resultado == [
        "verde",
        "verde",
        "gris",
        "verde",
        "verde",
    ]

@pytest.mark.parametrize(
    "palabra",
    [
        "PA2DA",
        "PAN-A",
        "PAN A",
        "🐼ANDA",
    ],
)
def test_rechaza_caracteres_invalidos(palabra):
    with pytest.raises(ValueError, match="solo letras"):
        evaluar(palabra, "PANDA")