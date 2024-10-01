#Python reconoce automaticamente el tipo de dato de mi variable
#Puedo pisar una variable con un int usando strings, es de tipado debil
#Concatenar variables con un espacio en el medio
variable = 1
variable2 = 2
print(variable, variable2)
#Crear varias variables a la vez en una sola linea (practica horrible)
var1, var2, var3 = 1, "Siche", 3

print("Soy:",var2,"cuento",var1,var3)

#Inicializar variables con stdin
variable_usuario = input("Ingrese un dato: ") #Podemos escribir texto que se mostrar
print(variable_usuario)

#Indicar como interpretar una variable
#Al forzar
entero: int = "Hola" #No porque este tipado lo tomara como error, es solo algo a nivel visual
string: str = "Cadena"
flotante: float = 2.4

