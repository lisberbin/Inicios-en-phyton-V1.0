# VARIABLES
# Lo ideal es declara e inicializar siempre las variables.
# -----------------------------------------------------------
# En Python podemos asignar una variabla otra variable diferente.
var = "Hola mundo"
var2 = var
print(var2)
#la variable var y var2 apuntan a la misma cadena de texto Hola mundo
#Los nombres de las variables en Pythonpueden tener cualquier longitud y
# pueden consistir en letras mayúsculas y minúsculas (A-Z, a-z), dígitos (0-9) y
# el carácter de subrayado (_). Cualquier otro carácter dará error:
#2var& = "Hola mundo"
#Aunque el nombre de una variable puede contener dígitos, el primer carácter de
# un nombre de variable no puede ser un dígito.
var = "Hola mundo"
#El nombre de las variables en Python essensible a mayúsculas y minúsculas
#Var3 = "Hola mundo"
#print(var3) #Error, no se encuentra var3
# Declaración de variable numérica entera:
n_edad = 47

# Declaración de variable numérica de coma flotante:
n_numero = -23.5245
# Declaración de variable de tipo string:
s_nombre = 'Manolo es "amigo" mío'
# Declaración de variable de tipo string en varias líneas:
s_textoLargo = """Esto es un mensaje
...con tres saltos
...de linea"""
# Sobreescribimos el valor de la variable s_edad y ahora la ponemos como string:
s_edad = "47"
# Declaración de constante:
NUMEROPI = 3.14159
# Declaración de un boolean
is_verdadero = True
is_casado = False
# True = 1 y False = 0
True == 1
False == 0
print(True + 2)
# Cuando se valida una condición , Python devuelve True o False:
print(10 > 9)
print(10 == 9)
print(10 < 9)
# Declaración múltiple
# En una sola instrucción, estamos declarando tres variables: a, b y c, y asignándoles un valor concreto a cada una.
a, b, c = 'string', 15, True
# Sería como poner:
a = 'string'
b = 15
c = True

