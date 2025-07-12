from random import choice
import sys

def mostrar_tablero(numeros):
    tateti = f"""
                ============================
                |        |        |        |
                |    {numeros[0]}   |    {numeros[1]}   |    {numeros[2]}   |
                |        |        |        |
                ============================
                |        |        |        |
                |    {numeros[3]}   |    {numeros[4]}   |    {numeros[5]}   |
                |        |        |        |           
                ============================
                |        |        |        |
                |    {numeros[6]}   |    {numeros[7]}   |    {numeros[8]}   |
                |        |        |        |
                ============================
                """
    print(tateti)

def numeros_disponibles(numeros):
    disponibles = []
    for disponible in numeros:
        # print(disponible)
        if disponible != "X" and disponible != "O":
            disponibles.append(disponible)
    
    return disponibles

def verificar_ganador(numeros, jugador):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]

    for combo in combinaciones:
        ganador = True
        for i in combo:
            if numeros[i] != jugador:
                ganador = False
                break
        if ganador:
            return True
    return False


numeros = [ "1", "2" , "3", "4" , "5", "6" , "7" , "8" , "9" ]
ocupados = []
while True:

    mostrar_tablero(numeros)

    while True:
        movimiento = input("Ingresa tu movimiento (1-9): ").strip()

        if movimiento not in numeros:
            print("Casilla inválida o ya ocupada.")
        else:
            break
            

    numeros[int(movimiento) - 1] = "X"
    ocupados.append(movimiento)
    mostrar_tablero(numeros)

    disponibles = numeros_disponibles(numeros)

    if verificar_ganador(numeros, "X"):
        mostrar_tablero(numeros)

        print("¡Ganaste!")
        salir = input("Desea volver a jugar? (s/n): ").lower().strip()
        if salir == "s":
            numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            ocupados = []
        else: 
            sys.exit()

    jugada_pc = choice(disponibles)
    print(f"La máquina elige la casilla {jugada_pc}")
    numeros[int(jugada_pc) - 1] = "O"
    ocupados.append(jugada_pc)


    if verificar_ganador(numeros, "O"):
        mostrar_tablero(numeros)
        print("La máquina ganó.")

        salir = input("Desea volver a jugar? (s/n): ").lower().strip()
        if salir == "s":
            numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            ocupados = []
        else: 
            break

    disponibles = numeros_disponibles(numeros)
    print(disponibles)