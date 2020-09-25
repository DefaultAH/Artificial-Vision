import os
from random import randint, uniform

def rand_integer():
    nz = randint(1,6)
    return nz
def juego():
    if i == 50:
        print("Nivel Básico (50 Casillas)")
    elif i == 70:
        print("Nivel Intermedio (70 Casillas)")
    else:
        print("Nivel Avanzado (100 Casillas)")
    sc = []
    p = int(input("Dijite cuantos jugadores desean jugar (Minimo 2, Maximo 5): "))
    for x in range(1, p+1):
        new = 0
        sc.append(new)
    x = 0
    while sc[x] <= i:
        os.system("cls")
        print("Jugador ", x+1)
        input("")
        d1 = rand_integer()
        d2 = rand_integer()
        print("Dado 1: " ,d1)
        print("Dado 2: " ,d2)
        sc[x] = sc[x] + d1 + d2
        print("Acumulado Jugaror " , x+1 ,": ",sc[x], " Puntos")
        print("Puntuacion de los jugadores: ", sc)
        input("")
        if sc[x] >= i:
            print("Ganador Jugador[",x+1,"]")
            input()
            break
        x = x + 1
        if x == p:
            x = 0
     
#menu

def menu():
    os.system('cls')
    print("Carrera de dados \n Seleccione el Nivel! \n 1. Nivel Básico (50 posiciones) \n 2. Nivel Intermedio (70 posiciones) \n 3. Nivel Avanzado (100 posiciones) \n 4. Salir \n")
menu()
choice = int(input("inserta un numero valor: "))
while True:
    if choice == 1:
        os.system('cls')
        i = 50
        juego()
        break
    elif choice == 2:
        i = 70
        juego()
        break
    elif choice == 3:
        i = 100
        juego()
        break
    elif choice == 4:
        break
    else:
        print("")
        print("No has pulsado ninguna opción correcta...")
        os.system('cls')
        menu()
        choice = input("inserta un numero valor: ")
        
