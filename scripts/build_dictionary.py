from argparse import ArgumentParser
from pathlib import Path

from wordfreq import top_n_list

from wordle.dictionary import preparar_palabras


def main() -> None:
    parser = ArgumentParser(
        description="Genera el diccionario español para Wordle."
    )
    parser.add_argument(
        "--limite",
        type=int,
        default=50_000,
        help="Cantidad de entradas solicitadas a wordfreq.",
    )
    parser.add_argument(
        "--salida",
        type=Path,
        default=Path("data/palabras.txt"),
        help="Archivo donde se guardará el diccionario.",
    )

    argumentos = parser.parse_args()

    candidatas = top_n_list("es", argumentos.limite)
    palabras = preparar_palabras(candidatas)

    argumentos.salida.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    argumentos.salida.write_text(
        "\n".join(palabras) + "\n",
        encoding="utf-8",
    )

    print(
        f"Diccionario generado: {len(palabras)} palabras "
        f"en {argumentos.salida}"
    )


if __name__ == "__main__":
    main()