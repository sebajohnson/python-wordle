from pathlib import Path

from wordle.text import normalizar, validar_caracteres

def cargar_palabras(ruta: str | Path) -> list[str]:
    contenido = Path(ruta).read_text(encoding="utf-8")
    palabras = []
    palabras_vistas = set()

    for linea in contenido.splitlines():
        palabra = normalizar(linea.strip())

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