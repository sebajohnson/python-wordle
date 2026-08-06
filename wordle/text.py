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

IDIOMA_PREDETERMINADO = "es"

ALFABETOS = {
    "es": frozenset("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"),
    "en": frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
}


def normalizar(palabra: str) -> str:
    return palabra.upper().translate(TRADUCCION_TILDES)


def validar_caracteres(
    palabra: str,
    idioma: str = IDIOMA_PREDETERMINADO,
) -> None:
    if idioma not in ALFABETOS:
        raise ValueError(f"Idioma no soportado: {idioma}")

    alfabeto = ALFABETOS[idioma]

    if not all(letra in alfabeto for letra in palabra):
        raise ValueError(
            f"La palabra debe contener solo letras "
            f"del alfabeto '{idioma}'"
        )