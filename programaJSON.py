#------------------------- Importacion de marvel.json ---------------------------

import json

with open("movies.json") as fichero:

    doc=json.load(fichero)

#--------------------------- Definicion de variables -----------------------------

dic_opcion1 = {}
dic_opcion2 = {}
dic_media_peliculas = {}

lista_actores = []
lista_peliculas_actores = []
lista_entre_años = []
lista_opcion5 = []

encontrado = False

import operator

#----------------------------- Listas y Dicionarios ------------------------------

for dic in doc:

    dic_opcion1[dic.get("title")] = [dic.get("year"), dic.get("duration")]


for dic in doc:

    dic_opcion2[dic.get("title")] = len(dic.get("actors"))


for dic in doc:

    for actor in dic.get("actors"):
        
        if actor not in lista_actores:
        
            lista_actores.append(actor)

lista_actores.sort()

#----------------------------------- Funciones -----------------------------------

def peliculas_actores(actor,doc):

    for dic in doc:

        if actor in dic.get("actors"):

            lista_peliculas_actores.append(dic.get("title"))

    return lista_peliculas_actores


def entre_años(año1, año2, doc):

    for año in range(año1,año2 + 1):

        lista_entre_años.append(str(año))

    for dic in doc:

        if dic.get("year") in lista_entre_años:

            media = sum(dic.get("ratings")) / len(dic.get("ratings"))

            dic_media_peliculas[media] = [dic.get("title"),dic.get("posterurl")]
    
    dic_ordenado = sorted(dic_media_peliculas.items(), key=operator.itemgetter(0))

    dic_ordenado.reverse()

    lista_opcion5.append(dic_ordenado[0])
    lista_opcion5.append(dic_ordenado[1])
    lista_opcion5.append(dic_ordenado[2])

    return lista_opcion5


#------------------------------------ Programa -----------------------------------

print("")
print("-------------------MENU--------------------")
print("(1) Listar titulo, año y duración de peliculas")
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
        print("Opcion 1 elegida (Te muestra el titulo, año y duración de todas las peliculas)")
        print("---------------------------------------------------------------------------------")
        print("")

        for titulo, lista in dic_opcion1.items():
            
            print("")
            print("Titulo:", titulo)
            print("Año:", lista[0])
            print("Duracion:", lista[1].replace("PT",""))
            print("")
            print("------------------------------------------")

    if opcion == 2:
        
        print("---------------------------------------------------------------------------------")
        print("Opcion 2 elegida (Te muestra los titulos de las peliculas y el numero de actores/actrices que tienen cada una)")
        print("---------------------------------------------------------------------------------") 
        print("")

        for titulo, numactor in dic_opcion2.items():

            print("")
            print("Pelicula:", titulo)
            print("Nº de actores/actrices:", numactor)
            print("")
            print("------------------------------------------")

    if opcion == 3:

        print("---------------------------------------------------------------------------------")
        print("Opcion 3 elegida (Haz una busqueda recursiva de la sinopsis y te muestra las peliculas)")
        print("---------------------------------------------------------------------------------")
        print("")

        palabra1 = input("Introduce una cadena para buscar: ")
        palabra2 = input("Introduce otra cadena para buscar: ")

        for dic in doc:

            if dic.get("storyline").count(palabra1) > 0:
                
                if dic.get("storyline").count(palabra2) > 0:

                    print("")
                    print("---------------------------------")
                    print("Pelicula:",dic.get("title"))
                    print("")
                    print("Descripcion:",dic.get("storyline"))
                    encontrado = True
                
        if encontrado == False:

            print("")
            print("----------------------------------")
            print("NO SE HAN ENCONTRADO COINCIDENCIAS")
            print("----------------------------------")

    if opcion == 4:

        print("---------------------------------------------------------------------------------")
        print("Opcion 4 elegida (Introduce un actor y te muestra las peliculas en las que ha trabajado)")
        print("---------------------------------------------------------------------------------")
        print("")

        print("")
        nom_actor = input("Introduce actor/actriz: ")   
        print("")    

        while nom_actor not in lista_actores:

            print("")
            print("--------------------------")
            print("ERROR, no existe actor/actriz")
            print("--------------------------")
            print("")

            nom_actor = input("Introduce actor/actriz: ")
        
        print("")
        print("El actor", nom_actor,"ha participado en:")
        print("")
        print("----------------Peliculas---------------")
        print("")

        for peliculas in peliculas_actores(nom_actor,doc):
            
            print(peliculas)
            
    if opcion == 5:

        print("---------------------------------------------------------------------------------")
        print("Opcion 5 elegida (Introduce dos fechas y te muestra el titulo y poster de las tres peliculas con la media mas alta)")
        print("---------------------------------------------------------------------------------")
        print("")

        print("")
        fecha1 = int(input("Introduce un año: "))
        fecha2 = int(input("Introduce otro año mayor: "))   
        print("")    

        while fecha1 > fecha2:

            print("")
            print("--------------------------")
            print("ERROR, introduce un año mayor")
            print("--------------------------")
            print("")

            fecha2 = int(input("Introduce otro año mayor: "))

        for dic in entre_años(fecha1,fecha2,doc):

            print("--------------------------")
            print("")
            print("Titulo:", dic[1][0],"con una media de puntuacion de",dic[0])
            print("")
            print("URL:", dic[1][1])
            print("")
            print("--------------------------")



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