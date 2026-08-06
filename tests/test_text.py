import pytest

from wordle.text import validar_caracteres


def test_espanol_permite_enie():
    validar_caracteres("NIÑO", idioma="es")


def test_ingles_rechaza_enie():
    with pytest.raises(ValueError, match="solo letras"):
        validar_caracteres("NIÑO", idioma="en")


def test_rechaza_idioma_no_soportado():
    with pytest.raises(ValueError, match="Idioma no soportado"):
        validar_caracteres("PANDA", idioma="hv")