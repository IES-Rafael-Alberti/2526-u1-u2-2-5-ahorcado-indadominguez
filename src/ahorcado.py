"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: [Indalecio Domínguez Hita]
Fecha: [06/11/2025]
"""


def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para simular la limpieza de pantalla,
    de forma que el jugador 2 no vea la palabra introducida por el jugador 1.
    """
    print("\n" * 50)


def solicitar_palabra():
    """
    Solicita una palabra al jugador 1.

    La palabra debe tener al menos 5 caracteres y solo puede contener letras.
    Se repetirá la solicitud hasta que se cumplan estas condiciones.

    Returns:
        str: La palabra a adivinar en mayúsculas.
    """

    palabra_valida = False

    while not palabra_valida:
        palabra = input("Jugador 1, introduzca la palabra a adivinar: ").strip()

        if len(palabra) < 5:
            print("La palabra debe de tener al menos 5 caracteres.") 
        elif not palabra.isalpha():
            print("La palabra solo puede contener letras.")
        else:
            palabra_valida = True

    return palabra.upper()


def solicitar_letra(letras_usadas):
    """
    Solicita una letra al jugador 2.

    La letra debe cumplir:
        - Ser una única letra (no números ni símbolos)
        - No haber sido usada anteriormente

    Args:
        letras_usadas (list): Lista con las letras ya introducidas.

    Returns:
        str: La letra introducida en mayúsculas.
    """

    letra_valida = False

    while not letra_valida:
        letra = input("Introduce una letra: ").strip().upper()

        if len(letra) != 1:
            print("Como máximo una letra.")
        elif not letra.isalpha():
            print("Solo se permiten letras.")
        elif letra in letras_usadas:
            print("Letra repetida, utiliza otra.")
        else:
            letra_valida = True

    return letra



def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego: intentos, palabra y letras usadas.

    Args:
        palabra_oculta (str): La palabra con guiones bajos y letras descubiertas.
        intentos (int): Número de intentos restantes.
        letras_usadas (list): Lista de letras que el jugador ya ha intentado.
    """
    print(f"\nIntentos restantes: {intentos}")
    print("Palabra: " + " ".join(palabra_oculta))
    print(f"Letras usadas: {', '.join(letras_usadas)}")
    
    print("==================================\n")


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de una letra correcta.

    Args:
        palabra (str): La palabra completa a adivinar.
        palabra_oculta (str): La palabra actual con guiones bajos y letras descubiertas.
        letra (str): La letra adivinada por el jugador.

    Returns:
        str: La palabra oculta actualizada con las letras descubiertas.
    """
    lista_oculta = list(palabra_oculta)

    for i in range(len(palabra)):
        if palabra[i] == letra:
            lista_oculta[i] = letra

    return "".join(lista_oculta)


def jugar():
    """
    Ejecuta una partida del juego del ahorcado.

    En esta función se gestiona el flujo principal del juego:
    - Se solicita la palabra a adivinar al Jugador 1.
    - Se inicializa la palabra oculta y los intentos disponibles.
    - Se solicitan letras al Jugador 2 hasta que gane o pierda.
    - Se muestra el estado del juego en cada intento.

    Returns:
        None
    """
    print("=== JUEGO DEL AHORCADO ===\n")

    INTENTOS_MAXIMOS = 5

    palabra = solicitar_palabra()

    limpiar_pantalla()

    palabra_oculta = "_" * len(palabra)
    intentos = INTENTOS_MAXIMOS
    letras_usadas = []
    juego_terminado = False

    print("Jugador 2: ¡Adivina la palabra!\n")

    while intentos > 0 and not juego_terminado:
        mostrar_estado(palabra_oculta, intentos, letras_usadas)

        letra = solicitar_letra(letras_usadas)
        letras_usadas.append(letra)

        if letra in palabra:
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            
            if "_" not in palabra_oculta:
                juego_terminado = True
                print("\n¡Felicidades! Has adivinado la palabra:", palabra)
        else:
            intentos -= 1
            print(f"La letra '{letra}' no está en la palabra.")
            if intentos == 0:
                print("\nTe has quedado sin intentos. La palabra era:", palabra)

def main():
    """
    Punto de entrada principal del programa.

    Llama a la función `jugar()` para iniciar una partida del ahorcado.
    Opcionalmente, se podría preguntar al usuario si desea jugar otra vez
    al finalizar la partida.

    Returns:
        None
    """
    jugar_otra_vez = "s"
    while jugar_otra_vez.lower() == "s":
        jugar()
        jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")

    print("\nGracias por jugar al Ahorcado. ¡Hasta pronto!")


if __name__ == "__main__":
    main()
