import os #Importamos OS para mas tarde poder borrar consola

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

class Ahorcado: #Creamos la clase "Ahorcado"
    def __init__ (self, palabra, letra): #definimos metodo constructor con los atributos palabra, letra, falses, vidas y text
        self.palabra = list(palabra)
        self.falses = []
        self.letra = letra
        self.vidas = 8
        self.text = [
                """









                _______________________\n
                """,
                """
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
                """, """
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
                """, """
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
                """, """
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
                """, """
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
                """, """
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
                """, """
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
                """
            ]
    def generar_lista_falses(self):
        """_summary_
            Este metodo consiste en generar una lista de valores falsos
            en funcion de la cantidad de caracteres que tenga la 
            palabra que nos introduzca el usuario.
        """
        for i in range(0, len(palabra)): #Bucle for que recorre un rango de la longitud de la palabra
            self.falses.append(False) #Añade valores "False" a la lista de la variable "Falses"
    
    def restar_vida(self):
        """_summary_
            Este metodo consiste en restar vidas .
        """
        self.vidas -= 1 #Esta linea borra las vidas
        os.system("cls") #Borra consola
        print("¡ Has fallado ! : Te queda una vida menos. Te quedan " + str(self.vidas) + " vidas restantes.") #Imprime la frase y las vidas que te quedan
        print(self.text[len(self.text) -1 - self.vidas]) #imprime el muñeco que toque
        
    def comprobar(self):
        """_summary_
            Este metodo consiste en comprobar la letra, te indica en que
            posicion se encontro y tambien comprueba si la palabra es
            correcta, y si esta correcta te imprime que has ganado.
        """
        if self.letra in self.palabra: #Bucle if que busca que esta la letra en la palabra 
            print("¡Correcto! : La letra: " + self.letra + " esta dentro de la palabra.") #Imprime que la letra esta en la palabra
            for i in range(0, len(self.palabra)): #Bucle for que recorre un rango en la longitud de la palabra:
                if self.palabra[i] == self.letra: #Compara  "i" en la palabra con la letra
                    os.system("cls") #Borra consola
                    print("Se encontro la letra en la posicion " + str(i)) #Imprime la posicion "i" donde se encontro la palabra
                    self.falses[i] = True #Convertimos esa letra que esta correcta a True
                    print(self.falses) #Imprimos la variable falses
                    if(False in self.falses) == False: #if que mira si hay valores "False" en la variable "Falses" y lo compara con "False"
                        os.system("cls") #Borra consola
                        print("Felicidades, has ganado, la palabra era:") #Imprime que has ganado
                        print(self.palabra) #Imprime la palabra
                        exit(0) #Sale del programa
        else: #Si la letra no es correcta se ejecuta la linea de abajo
            self.restar_vida() #Se ejecuta el metodo "restar_vida"
            
try: #Prueba si los valores introducidos son correctos
    palabra = list(input("Introduzca aqui la palabra: ")) #Pedimos que nos ingrese la palabra y la metemos en la variable "palabra"
except KeyboardInterrupt: #Si sale del programa desde el comando "ctrl + c" se imprime la linea de abajo
    print("Saliendo del programa...")

MyAhorcado = Ahorcado(palabra, "") #Creamos el objeto con los valores palabra y "" que en este caso las comillas seria para la variable letras

MyAhorcado.generar_lista_falses() #Llamamos a el metodo "generar_lista_falses" para que se ejecute y nos cree la lista de estos

while MyAhorcado.vidas >=1: #Hacemos un bucle while que mientra que las vidas sean mayor o igual que 1 haga:
    MyAhorcado.letra = input("Introduze aqui la letra: ") #Pide al usuario que introduzca la letra
    MyAhorcado.comprobar() #Llamamos a el metodo "comprobar" para que se ejecute