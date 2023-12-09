import os #Importamos OS para poder borrar la consola

print("Ahorcado Made By Koan")
print("""
        |----------|
        |          |
        |         _|_
        |        (x x)
        |        (___)
        |         | |
        |        /   \\
        |         | | 
        |         | |
        |________/___\\__________\n
        """)

try: #Aqui le pedimos al usuario que introduzca la palabra del juego
    palabra = list(input("Introduzca aqui la palabra: ")) #Metemos la palabra que nos indique el usuario como lista en la variable palabra
    falses = list() #Creamos la variable "falses" y metemos una lista
    for i in range(0, len(palabra)): #Hacemos un bucle for que recorra i en un rango que empieze en la posicion 0 y recorra la logintud de la palabra
        falses.append(False) #Hacemos que agregue falses con el metodo append
    vidas = 8 #Creamos la variable vidas y asignamos el valor de vidas que queremos que tenga
    letras_correctas = []
except KeyboardInterrupt: #Si el usuario aprieta ctrl + c se imprime la linea de abajo
    print("Saliendo del programa...")

print("La palabra tiene una longitud de: " + str(len(palabra)) + " caracteres.") #Imprimer la logintud de caracteres que tiene la palabra

def vida1(): #En este punto tienes todas las vidas
    print("""









        _______________________\n
        """)
def vida2(): #En este punto tienes 6 vidas
    print("""
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |_______________________\n
        """)
def vida3(): #En este punto tienes 5 vidas
    print("""
        |----------|
        |          |
        |          |
        |
        |
        |
        |
        |
        |
        |_______________________\n
        """)
def vida4(): #En este punto tienes 4 vidas
    print("""
        |----------|
        |          |
        |         _|_
        |        (. .)
        |        (___)
        |
        |
        |
        |
        |_______________________\n
        """)
def vida5(): #En este punto tienes 3 vidas
    print("""
        |----------|
        |          |
        |         _|_
        |        (. .)
        |        (___)
        |         | |
        |        
        |
        |
        |_______________________\n
        """)
def vida6(): #En este punto tienes 2 vidas
    print("""
        |----------|
        |          |
        |         _|_
        |        (. .)
        |        (___)
        |         | |
        |        /   \\
        |          
        |
        |_______________________\n
        """)
def vida7(): #En este punto tienes 1 vida
    print("""
        |----------|
        |          |
        |         _|_
        |        (. .)
        |        (___)
        |         | |
        |        /   \\
        |         | | 
        |         | |
        |_______________________\n
        """)
def vida8(): #En este punto ya has perdido
    print("""
        |----------|
        |          |
        |         _|_
        |        (x x)
        |        (___)
        |         | |
        |        /   \\
        |         | | 
        |         | |
        |________/___\\__________\n
        """)

vidasrestantes = [
    vida1,
    vida2,
    vida3,
    vida4,
    vida5,
    vida6,
    vida7,
    vida8,
]

while vidas >=1: #Hacemos un bucle while para que se repita:
    letra = input("Introduzca aqui la letra: ") #Declaramos la variable letra y pedimos que nos introduzca un valor como string
    if letra in palabra: #Hacemos un if determinando que si letra esta en la palabra se imprima que esta dentro 
        print("¡ Correcto ! : La letra: " + letra + " esta dentro de la palabra.")
        letras_correctas.append(letra) #Añadimos la letra a una variable que se llama letras_correctas
        for i in range(0, len(palabra)-1): #Hacemos un bucle for en el que i recorre un rango empezando por la posicion 0 recorra la longitud de palabra -1
            if palabra[i] == letra: #Hacemos un if que si i en la palabra es igual a la letra demuestre que esta en la posicion "x" de la palabra
                os.system("cls") #Borra consola
                print("se encontro la letra, en la posicion " + str(i))
                falses[i] = True #Añade un valor true a la variable de falses
                print(falses)
    else: #Si no encontro la letra resta 1 vida, borra consola y enseña el print del muñeco
        vidas -= 1
        os.system("cls")
        print("¡ Has fallado ! : Te queda una vida menos. Te quedan " + str(vidas) + " vidas restantes.")
        vidasrestantes [len(vidasrestantes) -1 - vidas]()
    
    if letras_correctas == palabra: #Este if nos servira para comprobar si las letras coinciden con la palabra, si son iguales se ejecuta:
        os.system("cls") #Borra consola
        print("Felicidades, has ganado, la palabra era:") #Imprime la frase
        print(palabra) #Imprime la palabra en forma de lista
        break #Sale del programa
