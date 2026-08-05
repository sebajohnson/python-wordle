TRADUCCION_TILDES = str.maketrans(
    {
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U",
        "Ü": "U",
    }
)

ALFABETO = frozenset("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")


def _normalizar(palabra: str) -> str:
    return palabra.upper().translate(TRADUCCION_TILDES)

def _validar_caracteres(palabra: str) -> None:
    if not all(letra in ALFABETO for letra in palabra):
        raise ValueError(
            "Las palabras deben contener solo letras del alfabeto español"
        )
def evaluar(intento: str, solucion: str) -> list[str]:
    intento = _normalizar(intento)
    solucion = _normalizar(solucion)

    if len(intento) != 5 or len(solucion) != 5:
        raise ValueError(
            "El intento y la solución deben tener cinco letras"
        )

    _validar_caracteres(intento)
    _validar_caracteres(solucion)

    resultado = ["gris"] * len(intento)
    letras_disponibles = list(solucion)

    # Primera pasada: posiciones correctas
    for indice, (letra_intento, letra_solucion) in enumerate(
        zip(intento, solucion)
    ):
        if letra_intento == letra_solucion:
            resultado[indice] = "verde"
            letras_disponibles[indice] = None

    # Segunda pasada: posiciones incorrectas
    for indice, letra_intento in enumerate(intento):
        if resultado[indice] == "verde":
            continue

        if letra_intento in letras_disponibles:
            resultado[indice] = "amarillo"
            letras_disponibles.remove(letra_intento)

    return resultado