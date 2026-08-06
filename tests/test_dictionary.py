from wordle.dictionary import cargar_palabras


def test_carga_palabras_unicas(tmp_path):
    archivo = tmp_path / "palabras.txt"

    archivo.write_text(
        "PANDA\nPLUMA\nPANDA\n\n",
        encoding="utf-8",
    )

    resultado = cargar_palabras(archivo)

    assert resultado == {"PANDA", "PLUMA"}