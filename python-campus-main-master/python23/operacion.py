operacion = True

v1 = 0

while operacion == True :
    print("1. suma \n2).resta \n3).multiplicacion \n4).division")
    operacion = input ( ":)-")


    if operacion == "1" :
        v1 = int(input("ingrese un numero1 : "))
        v2 = int(input("ingrese un numero2 : "))
        print(f"la suma de {v1} + {v2} = {v1+v2}")
        x = ("predsione ENTER para salir....")
        operacion = bool(operacion)
    if operacion == "2" :
        v1 = int(input("ingrese un numero1 : "))
        v2 = int(input("ingrese un numero2 : "))
        print(f"resta de {v1} - {v2} = {v1-v2}")
        x = ("predsione ENTER para salir....")
        operacion = bool(operacion)
    if operacion == "3" :
        v1 = int(input("ingrese un numero1 : "))
        v2 = int(input("ingrese un numero2 : "))
        print(f"la multiplicacion de {v1} * {v2} = {v1*v2}")
        x = ("predsione ENTER para salir....")
        operacion = bool(operacion)
    if operacion == "4" :
        v1 = int(input("ingrese un numero1 : "))
        v2 = int(input("ingrese un numero2 : "))
        print(f"la resta de {v1} // {v2} = {v1//v2}")
        x = ("predsione ENTER para salir....")
        operacion = bool(operacion)
