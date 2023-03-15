#sub listas: posicion 0.:primer quiz,1. segundo quiz,2.tercer quiz,3.cuarto quiz,4.primer trabajo, 5.segundo trabajo,6.tercer trabajo,7.primer parcial,8.segundo parcial,9.tercer parcial
matriculados =["Maria",[0,0,0,0,0,0,0,0,0,0],"Juan",[0,0,0,0,0,0,0,0,0,0],"Carlos",[0,0,0,0,0,0,0,0,0,0],"Sofia",[0,0,0,0,0,0,0,0,0,0],"Alejandra",[0,0,0,0,0,0,0,0,0,0]]
op = 0
while op != 5:
    print("1.Estudiantes matriculados\n2.Ingreso de notas (Quices)\n3.Ingreso de notas (Trabajos)\n4.Ingreso de notas (Parciales)\n5.Salir")
    op = int(input("Elija una opcion "))
    if(op == 1):
        estudiantesM = str(input("Ingrese el primer nombre del estudiante (Primera letra mayuscula) "))
        for item in matriculados:
            if(estudiantesM in item):
                print(f"El estudiante {estudiantesM} si esta matriculado")
                x = input("Press any key to continue")
    elif(op == 2):
        estudiantesM = str(input("Ingrese el primer nombre del estudiante (Primera letra mayuscula) "))
        for item in matriculados:
            if(estudiantesM in item):
                item[1][0] = input("Ingrese la nota obtenida en el primer quiz")
                item[1][1] = input("Ingrese la nota obtenida en el segundo quiz ")
                item[1][2] = input("Ingrese la nota obtenida en el tercer quiz")
                item[1][3] = input("Ingrese la nota obtenida en el cuarto quiz")
        