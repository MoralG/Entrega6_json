#------------------------- Importacion de marvel.json ---------------------------

import json

with open("marvel.json") as fichero:

    doc=json.load(fichero)

#----------------------------------------------------------------------------------

print("")
print("-------------------MENU--------------------")
print("(1) Listar titulo, año y duracion de peliculas")
print("(2) El numero de actores/actrices de cada pelicula")
print("(3) Buscar por la sinopsis")
print("(4) Peliculas en las que ha actuado un actor")
print("(5) Mostrar url del poster")
print("(0) Finalizar el programa")
print("-------------------------------------------")
print("")

opcion = int(input("¿Que opcion eliges?   "))

while opcion != 0:    

    if opcion == 1:         # opcion 1: lista heroes

        print("---------------------------------------------------------------------------------")
        print("Opcion 1 elegida (Te muestra to titulo, año y duracion de todas las peliculas)")
        print("---------------------------------------------------------------------------------")
        print("")
    


    if opcion == 2:
        
        print("---------------------------------------------------------------------------------")
        print("Opcion 2 elegida (Te muestra los titulos de las peliculas y el numero de actores/actrices que tienen cada una)")
        print("---------------------------------------------------------------------------------") 
        print("")

    if opcion == 3:

        print("---------------------------------------------------------------------------------")
        print("Opcion 3 elegida (Haz una busqueda recursiva en la descripcion y te muestra las peliculas)")
        print("---------------------------------------------------------------------------------")
        print("")

    if opcion == 4:

        print("---------------------------------------------------------------------------------")
        print("Opcion 4 elegida (Introduce un actor y te muestra las peliculas en las que ha trabajado)")
        print("---------------------------------------------------------------------------------")
        print("")

    if opcion == 5:

        print("---------------------------------------------------------------------------------")
        print("Opcion 5 elegida (Introduce dos fechas y te muestra el titulo y poster de las tres peliculas con la media mas alta)")
        print("---------------------------------------------------------------------------------")
        print("")

    if opcion < 0 or opcion > 5:

        print("-----------------------")
        print("ERROR, opcion no valida")
        print("-----------------------")

    print("")
    print("")
    print("")
    print("")
    print("")
    print("-------------------MENU--------------------")
    print("(1) Listar titulo, año y duracion de peliculas")
    print("(2) El numero de actores/actrices de cada pelicula")
    print("(3) Buscar por la sinopsis")
    print("(4) Peliculas en las que ha actuado un actor")
    print("(5) Mostrar url del poster")
    print("(0) Finalizar el programa")
    print("-------------------------------------------")
    print("")
    
    opcion = int(input("¿Que opcion eliges?   "))


print("-----------------------")
print("   FIN DEL PROGRAMA")
print("-----------------------")