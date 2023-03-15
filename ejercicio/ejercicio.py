nba = []
opcion = 0 
while opcion !=7:
    print("1.Registro de jugadores\n2.Estadisticas de jugadores\n3.Listado de jugadores por equipo\n4.Total canastas anotadas por equipo\n5.Promedio de asistencias por equipo\n6.Jugador que mayor numero de canastas anoto\n7.Salir")
    opcion = int(input("Elija una opcion "))
    if(opcion == 1):
        nombreEquipo = input("Ingrese nombre del equipo ")
        nombreJugador = input("Ingrese nombre del jugador ")
        dorsal = int(input("Ingrese numero de dorsal "))
        posicion = input("Ingrese la posicion del jugador ")
        edad = int(input("Ingrese la edad del jugador "))
        nba.append([nombreEquipo,nombreJugador,dorsal,posicion,edad,[0,0,0,0,0]])
    elif(opcion == 2):
        equipo = input("Ingrese nombre del equipo ")
        nrodorsal = int(input("Ingrese numero de dorsal del jugador "))
        for item in nba:
            if(equipo in item and nrodorsal in item):
                item[5][0] = float(input("Ingrese minutos jugados "))
                item[5][1] = int(input("Ingrese cantidad de asistencias "))
                item[5][2] = int(input("Ingrese cantidad de canastas "))
                item[5][3] = int(input("Ingrese cantidad de partidos jugados "))
                item [5][4] = item [5][2]*2
    elif(opcion == 3):
        equipo = input("Ingrese nombre del equipo")
        print("Nombre del jugador\t\tNumero de dorsal\t\tPosicion")
        for item in nba:
            if(equipo in item):
                print(f"{item[1]}\t\t\t\t{item[2]}\t\t\t\t{item[3]}")
                x = input("Press any key")
    elif(opcion == 4):
        equipo = input("Ingrese el nombre del equipo")
        totalcanastas = 0
        for item in nba:
            if (equipo in item):
                totalcanastas = totalcanastas+item[5][2]
                print(f"La cantidad de canastas de equipo {equipo} es: {totalcanastas}")
                x = input("Press any key")
    elif(opcion == 5):
        totalasistencias = 0
        totaljugadores = 0
        equipo = input("Ingrese el nombre del equipo")
        for item in nba:
            if(equipo in item):
                totalasistencias = totalasistencias+item[5][1]
                totaljugadores = totaljugadores+1
                print(f"El promedio de asistencias del equipo {equipo} es: {totalasistencias/totaljugadores}")
                x = input("Press any key")
    elif(opcion == 6):
        print("")   
print(nba)
