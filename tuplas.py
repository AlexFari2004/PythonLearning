#Son una coleccion de elementos inmutable
tupla = (1,1,"Hola",[1,2,"Siche"])
tupla[0] = 2 #No se puede porque es inmutable
tupla[3][0] = 2 #si se puede ya que estpy modificando una lista
print(tupla[3][0]) 