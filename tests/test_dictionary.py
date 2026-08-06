from wordle.dictionary import cargar_palabras, preparar_palabras


def test_prepara_palabras_segun_el_idioma():
    candidatas = ["house", "niños"]

    resultado_ingles = preparar_palabras(
        candidatas,
        idioma="en",
    )
    resultado_espanol = preparar_palabras(
        candidatas,
        idioma="es",
    )

    assert resultado_ingles == ["HOUSE"]
    assert resultado_espanol == ["HOUSE", "NIÑOS"]
    
def test_carga_palabras_unicas(tmp_path):
    archivo = tmp_path / "palabras.txt"

    archivo.write_text(
        "PANDA\nPLUMA\nPANDA\n\n",
        encoding="utf-8",
    )

    resultado = cargar_palabras(archivo)

    assert resultado == ["PANDA", "PLUMA"]

def test_normaliza_y_filtra_palabras_no_utilizables(tmp_path):
    archivo = tmp_path / "palabras.txt"

    archivo.write_text(
        "panda\n"
        "árbol\n"
        "CAMIÓN\n"
        "sol\n"
        "PA2DA\n"
        "PANDA\n",
        encoding="utf-8",
    )

    resultado = cargar_palabras(archivo)

    assert resultado == ["PANDA", "ARBOL"]