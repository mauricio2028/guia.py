edad = int(input("ingrese su edad : "))
if edad >= 0 and edad <= 1 :
    print("eres un bebe")
elif edad >= 2 and edad <= 11 :
    print("eres un niño")
elif edad >= 12 and edad <= 17 :
    print("eres un adolescente")
elif edad == 18 :
    print("mayor de edad")
elif edad >= 19 and edad <= 35:
    print("eres un joven adulto")
elif edad >= 36 and edad <= 55 :
    print("eres de mediana edad")
elif edad >= 56 and edad <= 90 :
    print("eres un  adulto mayor")
elif edad == 90:
    print("estas muy viejo")
else:
    print("el dato ingresado es erroneo")