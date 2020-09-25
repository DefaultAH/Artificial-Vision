import os
from random import randint, uniform

def rand_integer():
    nz = randint(1,6)
    return nz
#menu

def menu():
    print("Carrera de dados \n Seleccione el Nivel! \n 1. Nivel Básico (50 posiciones) \n 2. Nivel Intermedio (70 posiciones) \n 3. Nivel Avanzado (100 posiciones) \n")
    choice = input()

    if choice == "1":
        p1 = 0
        p2 = 0
        print("Nivel Básico (50 Casillas)")
        while p1 <= 50 or p2 <= 50:
            os.system("cls")
            print("Jugador 1   | Jugador 2")
            d1j1 = rand_integer()
            d2j1 = rand_integer()
            d1j2 = rand_integer()
            d2j2 = rand_integer()
            print("Dado 1: " ,d1j1, "| Dado 1: ", d1j2)
            print("Dado 2: " ,d2j1, "| Dado 2: ", d2j2)
            p1 += d1j1 + d2j1
            p2 += d1j2 + d2j2
            print("Acumulado: ",p1," | Acumulado: ",p2)
            if p1 >= 50:
                print ("El jugador 1 ha ganado!!!")
                break
            if p2 >= 50:
                print ("El jugador 2 ha ganado!!!")
                break           
    if choice == "2":
        p1 = 0
        p2 = 0
        print("Nivel Intermedio (70 Casillas)")
        while p1 <= 70 or p2 <= 70:
            os.system("cls")
            print("Jugador 1   | Jugador 2")
            d1j1 = rand_integer()
            d2j1 = rand_integer()
            d1j2 = rand_integer()
            d2j2 = rand_integer()
            print("Dado 1: " ,d1j1, "| Dado 1: ", d1j2)
            print("Dado 2: " ,d2j1, "| Dado 2: ", d2j2)
            p1 += d1j1 + d2j1
            p2 += d1j2 + d2j2
            print("Acumulado: ",p1," | Acumulado: ",p2)
            if p1 >= 70:
                print ("El jugador 1 ha ganado!!!")
                break
            if p2 >= 70:
                print ("El jugador 2 ha ganado!!!")
                break
    if choice == "3":
        p1 = 0
        p2 = 0
        print("Nivel Avanzado (50 Casillas)")
        while p1 <= 100 or p2 <= 100:
            os.system("cls")
            input("Jugador 1   | Jugador 2")
            d1j1 = rand_integer()
            d2j1 = rand_integer()
            d1j2 = rand_integer()
            d2j2 = rand_integer()
            print("Dado 1: " ,d1j1, "| Dado 1: ", d1j2)
            print("Dado 2: " ,d2j1, "| Dado 2: ", d2j2)
            p1 += d1j1 + d2j1
            p2 += d1j2 + d2j2
            print("Acumulado: ",p1," | Acumulado: ",p2)
            if p1 >= 100:
                input ("El jugador 1 ha ganado!!!")
                os.system("cls")
                menu()
            if p2 >= 100:
                input ("El jugador 2 ha ganado!!!")
                os.system("cls")
                menu()
                
menu()





