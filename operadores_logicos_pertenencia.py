#Operadores logicos and or not
print("Hola" == "Chau" and "hola" != "Chau") #Se deben cumplir ambas para que se verdadero
print("Hola" == "Chau" or "hola" != "Chau") #Con que se cumpla una ya es verdadero
print(not ("Hola" == "Chau") ) #Niega algo, si es true ahora lo toma como false, si era false ahora es true

#Operadores de pertenencia in y not in
cadena = "Hola mundo"
print("hola" in cadena) #False porque no 'h' esta en minuscula es sensible al case
print("Hola" in cadena) #True

print("siche" not in cadena) #True siche no esta en cadena