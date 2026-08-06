from argparse import ArgumentParser
from pathlib import Path

from wordfreq import top_n_list

from wordle.dictionary import preparar_palabras
from wordle.text import ALFABETOS, IDIOMA_PREDETERMINADO


def main() -> None:
    parser = ArgumentParser(
        description="Genera un diccionario para Wordle."
    )
    parser.add_argument(
        "--idioma",
        choices=sorted(ALFABETOS),
        default=IDIOMA_PREDETERMINADO,
        help="Idioma del diccionario.",
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
        default=None,
        help="Archivo de salida opcional.",
    )

    argumentos = parser.parse_args()

    salida = argumentos.salida

    if salida is None:
        salida = (
            Path("data")
            / argumentos.idioma
            / "palabras.txt"
        )

    candidatas = top_n_list(
        argumentos.idioma,
        argumentos.limite,
    )
    palabras = preparar_palabras(
        candidatas,
        idioma=argumentos.idioma,
    )

    salida.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    salida.write_text(
        "\n".join(palabras) + "\n",
        encoding="utf-8",
    )

    print(
        f"Diccionario '{argumentos.idioma}' generado: "
        f"{len(palabras)} palabras en {salida}"
    )


if __name__ == "__main__":
    main()