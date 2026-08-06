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


def normalizar(palabra: str) -> str:
    return palabra.upper().translate(TRADUCCION_TILDES)


def validar_caracteres(palabra: str) -> None:
    if not all(letra in ALFABETO for letra in palabra):
        raise ValueError(
            "Las palabras deben contener solo letras del alfabeto español"
        )