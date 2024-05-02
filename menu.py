from diccionario import Diccionario
import os

def imprimir_titol():
    titol = """

                                                    ______ _   _ _ _ _                    _        _                                              _
                                                    |  ____| | | | (_) |                  | |      | |               /\                          (_)
                                                    | |__  | | | | |_| |__  _ __ ___    __| | ___  | | ___  ___     /  \   ___ ___ ___ _ __   ___ _  ___  _ __  ___ 
                                                    |  __| | | | | | | '_ \| '__/ _ \  / _` |/ _ \ | |/ _ \/ __|   / /\ \ / __/ __/ _ \ '_ \ / __| |/ _ \| '_ \/ __|
                                                    | |____| | | | | | |_) | | |  __/ | (_| |  __/ | |  __/\__ \  / ____ \ (_| (_|  __/ |_) | (__| | (_) | | | \__ |
                                                    |______|_| |_|_|_|_.__/|_|  \___|  \__,_|\___| |_|\___||___/ /_/    \_\___\___\___| .__/ \___|_|\___/|_| |_|___/
                                                                                                                                          | |
                                                                                                                                          |_|

    """
    print(titol)


def menu():
    diccionario = Diccionario()
    while True:
        imprimir_titol()
        print("\nMenú:")
        print("1. Afegir entrada")
        print("2. Mostrar entrada")
        print("3. Modificar entrada")
        print("4. Eliminar entrada")
        print("5. Sortir")
        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            paraula = input("Introdueix la paraula: ")
            entrada = input("Introdueix la entrada de la paraula desitjada: ")
            os.system('cls')
            diccionario.agregar_palabra(paraula, entrada)
        elif opcio == "2":
            paraula = input("Introdueix la paraula: ")
            os.system('cls')
            diccionario.mostrar_entradas(paraula)
        elif opcio == "3":
            paraula = input("Introdueix la paraula: ")
            i = int(input("Introdueix el índex de la entrada a modificar[0,1,2,3,4...]: "))
            novaEntrada = input("Introduce la nova entrada: ")
            os.system('cls')
            diccionario.modificar_entrada(paraula, i, novaEntrada)
        elif opcio == "4":
            paraula = input("Introdueix la paraula: ")
            i = int(input("Introdueix el índex de la entrada a modificar[0,1,2,3,4...]: "))
            os.system('cls')
            diccionario.eliminar_entrada(paraula, i)
        elif opcio == "5":
            print("Has sortir correctament del programa.")
            break
        else:
            print("Opció no vàlida.")


if __name__ == "__main__":
    menu()
