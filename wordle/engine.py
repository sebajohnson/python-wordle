from wordle.text import normalizar, validar_caracteres

def evaluar(intento: str, solucion: str) -> list[str]:
    intento = normalizar(intento)
    solucion = normalizar(solucion)

    if len(intento) != 5 or len(solucion) != 5:
        raise ValueError(
            "El intento y la solución deben tener cinco letras"
        )

    validar_caracteres(intento)
    validar_caracteres(solucion)

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