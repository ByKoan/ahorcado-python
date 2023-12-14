# ahorcado-python
Este programa consta de el clasico juego Ahorcado programado en python a base de funciones, estoy trabajando en programarle en POO

#AHORCADO SIN POO
Funcionamiento - "python ahorcado_sin_poo.py"

---Variables---
palabra = la palabra que se va a intentar adivinar
letra = te pide que ingreses una letra
letras_correctas = añadimos las letras que esten correctas en la palabra aqui
falses = convertimos todas las letras de la palabra en cuanto nos la ingresen en falsas, y una vez que vaya respondiendo se convierten a trues
vidas = las vidas de las que dispones

#AHORCADO CON POO
Funcionamiento - "python ahorcado_con_poo.py"

---Programa---
Contamos con la clase Ahorcado, esta tiene los atributos: 
-Palabra 
-Falses
-Letra
-Vidas
-Text (Son los muñecos que se imprimen cada vez que se quita una vida)

Una vez declarados en el metodo constructor contamos con los siguientes metodos:
generar_listas_falsas : Como bien indica el nombre le usaremos para crear una lista con valores falsos de los caracteres que tenga la palabra
restar_vida : Este metodo se encarga de restar vidas si esta mal la letra indicada
comprobar : Este metodo comprueba si la letra esta bien, cambia su valor a True si es correcta, y cuando estan todas las letras de la palabra se encarga de mostrarte que ganaste.
