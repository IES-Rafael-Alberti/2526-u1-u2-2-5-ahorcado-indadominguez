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
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)


def solicitar_palabra():
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns:
        str: La palabra a adivinar en mayúsculas
    """

    palabra_valida = False

    while not palabra_valida:
        palabra = input("Jugador 1, introduzca la palabra a adivinar ").strip()

        if len(palabra) < 5:
            print("La palabra debe de tener al menos 5 caracteres.") 
        elif not palabra.isalpha():
            print("La palabra solo puede contener letras.")
        else:
            palabra_valida = True

    return palabra.upper()


def solicitar_letra(letras_usadas):
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Args:
        letras_usadas (list): Lista de letras ya introducidas
        
    Returns:
        str: La letra introducida en mayúsculas
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
    Muestra el estado actual del juego
    
    Args:
        palabra_oculta (str): La palabra con _ y letras adivinadas
        intentos (int): Número de intentos restantes
        letras_usadas (list): Lista de letras ya usadas
    """
    print("\n==================================")
    print(f"Intentos restantes: {intentos}")
    print(f"Palabra: {' '.join(palabra_oculta)}")
    
    if len(letras_usadas) == 0:
        print("Letras usadas: ninguna")
    else:
        print("Letras usadas:", ", ".join(letras_usadas))
    
    print("==================================\n")


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Args:
        palabra (str): La palabra completa a adivinar
        palabra_oculta (str): La palabra actual con _ y letras adivinadas
        letra (str): La letra que se ha adivinado
        
    Returns:
        str: La palabra oculta actualizada
    """
    lista_oculta = list(palabra_oculta)

    for i in range(len(palabra)):
        if palabra[i] == letra:
            lista_oculta[i] = letra

    return "".join(lista_oculta)


def jugar():
    """
    Función principal que ejecuta el juego del ahorcado.
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
    Punto de entrada del programa
    """
    jugar_otra_vez = "s"
    while jugar_otra_vez.lower() == "s":
        jugar()
        jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")

    print("\nGracias por jugar al Ahorcado. ¡Hasta pronto!")


if __name__ == "__main__":
    main()
