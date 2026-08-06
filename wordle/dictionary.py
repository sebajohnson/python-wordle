from collections.abc import Iterable
from pathlib import Path

from wordle.text import normalizar, validar_caracteres

def preparar_palabras(candidatas: Iterable[str]) -> list[str]:
    palabras = []
    palabras_vistas = set()

    for candidata in candidatas:
        palabra = normalizar(candidata.strip())

        if len(palabra) != 5:
            continue

        try:
            validar_caracteres(palabra)
        except ValueError:
            continue

        if palabra in palabras_vistas:
            continue

        palabras.append(palabra)
        palabras_vistas.add(palabra)

    return palabras


def cargar_palabras(ruta: str | Path) -> list[str]:
    contenido = Path(ruta).read_text(encoding="utf-8")

    return preparar_palabras(contenido.splitlines())