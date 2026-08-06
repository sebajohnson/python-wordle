from pathlib import Path

from wordle.text import normalizar, validar_caracteres

def cargar_palabras(ruta: str | Path) -> set[str]:
    contenido = Path(ruta).read_text(encoding="utf-8")
    palabras = set()

    for linea in contenido.splitlines():
        palabra = normalizar(linea.strip())

        if len(palabra) != 5:
            continue

        try:
            validar_caracteres(palabra)
        except ValueError:
            continue

        palabras.add(palabra)

    return palabras