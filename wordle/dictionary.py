from pathlib import Path


def cargar_palabras(ruta: str | Path) -> set[str]:
    contenido = Path(ruta).read_text(encoding="utf-8")
    palabras = set()

    for linea in contenido.splitlines():
        palabra = linea.strip()

        if palabra:
            palabras.add(palabra)

    return palabras