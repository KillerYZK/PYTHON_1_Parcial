"""Practica 1: Cajero Automático    
Isaac Echeverría Álvarez
3a TPO
"""

#definir funciones que utlizara el programa
def mostrar_menu():
    print("------------------------------------")
    print("|Bienvenido a su cajero automatico |")
    print("------------------------------------")
    print("|1.Consultar saldo                 |")
    print("|2.Retirar efectivo                |")
    print("|3.Depositar efectivo              |")
    print("|4.Salir                           |")
    print("------------------------------------")
#funcion para depositar dinero
def depositar(saldo, deposito):
    print("-------------------------------------")
    print("|         Depositar efectivo        |")   
    print("-------------------------------------")
    print("|Cuanto dinero le vas a soltar?:    |")
    try:
        deposito = float(input())
        if deposito <= 0:
            print("El depósito debe ser mayor a cero")
            return saldo
        saldo += deposito
        print(f"|Has depositado: ${deposito:.2f}    |")
        print(f"|Tu saldo actual es de: ${saldo:.2f}|")
        print("------------------------------------")
    except ValueError:
        print("Por favor, ingrese una cantidad válida")
    return saldo
#funcion para sacar dinero
def saldo_restante(saldo, retirar):
    print("--------------------------------------------")
    print("|         Retirar efectivo                 |")
    print("--------------------------------------------")
    print("|Cuanto desea retirar?:                    |")
    try:
        retirar = float(input())
        if retirar <= 0:
            print("El retiro debe ser mayor a cero")
            return saldo
        if retirar > saldo:
            print("--------------------------------------------")
            print("|Insuficiencia de economia                 |")
            print("|Intenta con una cantidad mas pobre        |")
            print("--------------------------------------------")
            return saldo
        saldo = saldo - retirar
        print("--------------------------------------------")
        print(f"|Has retirado: ${retirar:.2f} de tu cuenta |")
        print(f"|Tu saldo actual es de: ${saldo:.2f}       |")
        print("--------------------------------------------")
    except ValueError:
        print("Por favor, ingrese una cantidad válida")
    return saldo

def main():
    # Pantalla de bienvenida
    print("------------------------------------")
    print("|Bienvenido a su cajero automatico |")
    print("------------------------------------")
    print("|            7 8 9                 |")
    print("|            4 5 6                 |")
    print("|            1 2 3                 |")
    print("|             0                    |")
    print("------------------------------------")
    
    pin_clave = 1234
    intentos = 3
    saldo = 1000.00

    # Validación del PIN
    while intentos > 0:
        try: 
            pin = int(input("Introduce tu PIN: "))
            if pin == pin_clave:
                print("------------------------------------")
                print("|Pin correcto, bienvenido al cajero |")
                print("------------------------------------")
                break
            else:
                intentos -= 1
                print("------------------------------------------")
                print("|Te equivocaste de PIN, intente de nuevo |")
                print(f"|Te quedan {intentos} intentos           |")
                print("------------------------------------------")
                if intentos == 0:
                    print("------------------------------------------")
                    print("|Te has equivocado demasiadas veces      |")
                    print("|Por favor, vuelve a intentarlo mas tarde|")
                    print("------------------------------------------")
                    exit()
        except ValueError:
            print("---------------------------------------")
            print("|Por favor, introduce un numero valido|")
            print("---------------------------------------")

    # Menú principal
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 4:        
                print("------------------------------------")
                print("|Elije algo valido no te pases.    |")
                print("------------------------------------")
                continue
            """
            Yo se que para esto se usa el if y el elif
            pero seamos honestos maestra,
            se ve bien feo con puros if (almenos a mi no me gusta mucho)
            entonces haciendo caso a lo que me dijo la maestra
            use el match B)
            """
            match opcion:
                case 1:
                    print("------------------------------------")
                    print("|              Su saldo            |")
                    print("------------------------------------")
                    print(f"|Su saldo es de: ${saldo:.2f}     |")
                    print("------------------------------------")
                case 2:
                    saldo = saldo_restante(saldo, 0)
                case 3:
                    saldo = depositar(saldo, 0)
                case 4:
                    print("------------------------------------")
                    print("|Gracias por usar nuestro cajero   |")
                    print("------------------------------------")
                    break
        except ValueError:
            print("---------------------------------------")
            print("|Por favor, introduce un numero valido|")
            print("---------------------------------------")

"""
honestamente me puse a medio investigar y encontre esto que esta abajito
Me preguntara y para que fregados es
Bueno esto sirve para actuar como punto de entrada del programa
y evitar que ciertas partes del código se ejecuten cuando el archivo es importado como módulo en
otro archivo.
palabreas mas o palabreas menos
Inicia el programa si lo ejecutas con directamente
"""

if __name__ == "__main__":
    main()