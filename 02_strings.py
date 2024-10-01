#Los string son objetos con atributos y metodos, por eso las cosas que haremos con las cadenas tendran cadena.metodo()
#Ver todas las cosas que modemos hacer con nuestro objeto, todos los metodos de mi clase string
dir(str) #Devuelve todos los metodos del TDA str
print(dir(str)) #Mostramos los metodos

#Mostrar cantidad de caracteres
cadena = "Hola mundo!"
caracteres = len(cadena)
print(caracteres)

#Concatenar variables
cadena1 = "Hola"
cadena2 = " Mundo"
print(cadena1 + cadena2)
    #No pudo concatenar tipos de datos diferentes
entero = 2
print(cadena1 + entero) #Al estar sobrecargado +, lo interpreta como una suma para el entero y como una concatenacion para el string

#Transformar un dato de otro tipo a string
numero = 10
numero_cadena = str(numero) #Ahora lo interpreta como caracteres
print(cadena1 + str(numero)) #Ahora si nos deja mostrar

#Mostrar un caracter o string repetidas veces
print(cadena1 * 4) #Mostrar hola varias veces, pero no funciona con float por obvias razones, no vas a mostrar hola partido a la mitad
print(cadena1 * 2.5) #No funciona
print(cadena1 * int(2.5)) #Casteamos, lo cual dejara la parte entera 

#Intepratar alfabeticamente 
print("hola" < "juan") #Se basa en ASCII, decolvera true porque h esta antes que la j por lo que es menor
print("aaaa" == "hola") #Muestra false


#Escape secuences
print("Hola" + " " + "Chau"+"\nsalto") #Uso el \n
print("Hola" + " " + "Chau"+"\\nsalto") #Al poner doble barra toma \n de forma litera, tambien puedo usar \t

#Mostrar una cantidad definida de caracteres de una cadena [inicio : final_sin_incluir : cada_cuanto]
texto = "Hola como va"
print(texto[ len(texto) -1 : 1 : -1 ]) #Le dije que empiece en el ultimo caracter -1, que vaya hasta el que esta en la posicion 1 sin incluirlo y que vaya en sus caracteres anteriores, si pusiera 1, iria con los siguiente

print(texto[::-1]) #Reconoce automaticamente que debe partir desde atras para adelante, mostrar una cadena al reves

#Mostrar posiciones de mi cadena
texto = "Siche"
caracter_pos_2 = texto[-1] #Guarda la ultima pos de texto, de atras para adelante empezamos en -1
print(caracter_pos_2)

#Contar la cantidad de veces que aparece un sub string o caracter en cadena original

cadena = "alacena"
print(cadena.count("a")) #Cuantas veces aparece la letra a en cadena, 3 veces
print(cadena.count("cena")) #1 vez sola

#Volver todo un string en mayuscula
cadena = "Hola"
print(cadena.upper()) #HOLA

#Volver todo un string en minuscula
cadena = "HOLA"
print(cadena.lower()) #hola

#Agregar la mayuscula al comienzo de mi string y volviendo todos los otros caracteres en minuscula
cadena = "hoLA"
print(cadena.capitalize()) #Hola

#Identificar si una cadena esta compuesta unicamente por caracteres numericos
cadena1 = "1236573"
cadena2 = "Hola123"
print(cadena1.isnumeric()) #True
print(cadena2.isnumeric()) #False

#Asi como existe para comprobar si es un numero, hay un monton mas:
#Para ver si todos los caracteres son en mayuscula
print("HOLA".isupper())

#Concatenar operaciones

print("hola".upper().isupper()) #Primero lo hace en mayuscula, luego verifica si lo esta, obvio que si

#Verificar si mi cadena empieza con cierta sub-cadena o caracter
print("Aventura".startswith("Aven")) #True

#Devolver en posicion se encuentra la primera aparicion de mi sub cadena
cadena = "Hola mundo"
print(cadena.find("H")) #Devolvera 0
print(cadena.find("mundo")) #Devolvera 5 devolviendo la posicion del primer caracter de mi subcadena
print(cadena.find("chau")) #Devolvera -1 indicando que no la encontro
print(cadena.index("Siche")) #index hace lo mismo que find, pero si no encuentra nada devulve un error

#Reemplazar todas las sub cadenas de mi cadena por otra sub cadena o caracter
cadena = "Aaaaaa eeee"
print(cadena.replace("a","b")) #Abbbbb eeee

#Separar mi cadena bajo un delimitador que elijamos

cadena = "Hola;como;va" 
lista = cadena.split(";") #Me devolvera una lista con elementos de cadena separados con el delimitador que elejimos
#lista = [Hola,como,va]