#Opcion 1, parecido a C
edad = 20
nombre = "Alex"
print("Mi edad es %d y mi nombre %s" %(edad,nombre)) #Evitamos la coma y para que considere las variables usamos %()

#Opcion 2, con {}
print("Mi edad es {} y mi nombre {}" .format(edad,nombre)) #Siempre con las variables ordenados

#opcion 3, con {} simplificada y la mejor
print(f"Mi edad es {edad} y mi nombre {nombre}") # f"{}"
