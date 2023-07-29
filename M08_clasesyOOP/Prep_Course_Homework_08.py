#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:
class Vehículo:
    def __init__(self,color,tipo,cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje



# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:
class VehículoMotorizado(Vehículo):
    def __init__(self, color, tipo, cilindraje):
        super().__init__(color, tipo, cilindraje)
        self.velo = 0
        self.doblar = 0
    def Acelerar(self, vel):
        self.velo += vel
    def Frenar(self, vel):
        self.velo -= vel
    def Doblar(self, grados):
        self.doblar += grados




# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:

mi_auto = VehículoMotorizado("Rojo", "auto", 1)
mi_camioneta = VehículoMotorizado("Azul", "camioneta", 5)
mi_camion = VehículoMotorizado("Blanco", "camion", 12)

mi_camion.Acelerar(20)
mi_camion.Frenar(30)
mi_camion.Doblar(30)

mi_auto.Acelerar(70)
mi_auto.Frenar(40)
mi_auto.Doblar(35)

mi_camioneta.Acelerar(50)
mi_camioneta.Frenar(60)
mi_camioneta.Doblar(38)
print(mi_camion.color, mi_camion.tipo, mi_camion.cilindraje)
print(mi_auto.color, mi_auto.tipo, mi_auto.cilindraje)
print(mi_camioneta.color, mi_camioneta.tipo, mi_camioneta.cilindraje)



# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:

class Datos(VehículoMotorizado):
    def Estado(self):
        print("Velocidad: ",self.velo,"Dirección: ", self.doblar)
    def Identificación(self):
        print("Color: ",self.color,"Tipo de vehículo: ", self.tipo,"Cilindraje: ", self.cilindraje)
mi_auto = Datos("rojo","auto",1)
mi_auto.Acelerar(70)
mi_auto.Frenar(40)
mi_auto.Doblar(35)
mi_auto.Estado()
mi_auto.Identificación()




# In[13]:
class Funciones:
    def __init__(self) -> None:
        pass
    def es_primo(self,numero):
        if numero==2 or numero==3 or numero==5:
            return(True)
        elif numero%2==0 or numero%3==0 or numero%5==0 :
            return(False)
        else:
            return(True)
    def son_primos(self,numeros):
        primos= []
        for i in numeros:
            if self.es_primo(i):
                primos.append(i)
        return primos
    def mas_repetido(self,i):
        conteo={}
        for x in i:
            if x in conteo:
                conteo[x]+=1
            else:
                conteo[x]=1
        valor_max=0
        dato= 0
        for x in conteo:
            if conteo[x]>= valor_max:
                valor_max=conteo[x]
                dato = x
        return("El número más repetido es ",dato," con:",valor_max," repeticiones.")
    def Conversor(self,valor,origen,destino):
        x=0
        if origen == "C" and destino == "F":
            x=(valor*(9/5)+32)
        elif origen == "C" and destino == "K":
            x=valor+273.15
        elif origen == "F" and destino == "C":
            x=(valor-32)/(9/5)
        elif origen == "K" and destino == "C":
            x=valor-273.15
        elif origen == "F" and destino == "K":
            x=(valor+459.67)*(5/9)
        else:
            x=1.8*(valor-273.15)+32
        return("El resultado de la conversión es:", x)
    def factorial(self, numero):
        while numero < 0:
            numero = -numero
        while isinstance(numero, float):
            numero = int(numero)
        if numero == 1:
            return 1
        elif numero >1:
            return numero * self.factorial(numero - 1)
        else:
            return "Valor Invalido"





# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:
class Funciones:
    def __init__(self) -> None:
        pass
    def es_primo(self,numero):
        if numero==2 or numero==3 or numero==5:
            return(True)
        elif numero%2==0 or numero%3==0 or numero%5==0 :
            return(False)
        else:
            return(True)
    def son_primos(self,numeros):
        primos= []
        for i in numeros:
            if self.es_primo(i):
                primos.append(i)
        return primos
    def mas_repetido(self,i):
        conteo={}
        for x in i:
            if x in conteo:
                conteo[x]+=1
            else:
                conteo[x]=1
        valor_max=0
        dato= 0
        for x in conteo:
            if conteo[x]>= valor_max:
                valor_max=conteo[x]
                dato = x
        return("El número más repetido es ",dato," con:",valor_max," repeticiones.")
    def Conversor(self,valor,origen,destino):
        x=0
        if origen == "C" and destino == "F":
            x=(valor*(9/5)+32)
        elif origen == "C" and destino == "K":
            x=valor+273.15
        elif origen == "F" and destino == "C":
            x=(valor-32)/(9/5)
        elif origen == "K" and destino == "C":
            x=valor-273.15
        elif origen == "F" and destino == "K":
            x=(valor+459.67)*(5/9)
        else:
            x=1.8*(valor-273.15)+32
        return("El resultado de la conversión es:", x)
    def factorial(self, numero):
        while numero < 0:
            numero = -numero
        while isinstance(numero, float):
            numero = int(numero)
        if numero == 1:
            return 1
        elif numero >1:
            return numero * self.factorial(numero - 1)
        else:
            return "Valor Invalido"





# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:

Lista1= [1,2,3,4,5,6,7,8,9,101,2,3,4,5,6,7,8,9,10,11,12,3,3,2,2,1,54,1,2,2,3,4,5]
Lista2= [0,"K","C"],[0,"C","K"],[0,"C","F"],[0,"F","K"],[0,"F","C"],[0,"K","F"]
primos= Funciones().son_primos(Lista1)
ValorModal= Funciones().mas_repetido(Lista1)
ConversorGrados=[]
ValorFactorial=[]
for i in Lista2: 
    ConversorGrados.append(Funciones().Conversor(*i))
for i in Lista1:
    ValorFactorial.append(Funciones().factorial(i))
print(primos)
print(ValorModal)
print(ConversorGrados)
print(ValorFactorial)



# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:
class Funciones:
    def __init__(self,listas):
        self.lista = listas
    def __es_primo(self,numero):
        if numero==2 or numero==3 or numero==5:
            return(True)
        elif numero%2==0 or numero%3==0 or numero%5==0 :
            return(False)
        else:
            return(True)
    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__Conversor(i, origen, destino),'grados',destino)
    def son_primos(self,numeros):
        primos= []
        for i in numeros:
            if self.__es_primo(i):
                primos.append(i)
        return primos
    def mas_repetido(self):
        conteo={}
        for x in self.lista:
            if x in conteo:
                conteo[x]+=1
            else:
                conteo[x]=1
        valor_max=0
        dato= 0
        for x in conteo:
            if conteo[x]>= valor_max:
                valor_max=conteo[x]
                dato = x
        return("El número más repetido es ",dato," con:",valor_max," repeticiones.")
    def factorial(self):
        for i in self.lista:
            print('El factorial de', i, 'es', self.__factorial(i))
    def __Conversor(self,valor,origen,destino):
        x=0
        if origen == "C" and destino == "F":
            x=(valor*(9/5)+32)
        elif origen == "C" and destino == "K":
            x=valor+273.15
        elif origen == "F" and destino == "C":
            x=(valor-32)/(9/5)
        elif origen == "K" and destino == "C":
            x=valor-273.15
        elif origen == "F" and destino == "K":
            x=(valor+459.67)*(5/9)
        else:
            x=1.8*(valor-273.15)+32
        return("El resultado de la conversión es:", x)
    def __factorial(self, numero):
        while numero < 0:
            numero = -numero
        while isinstance(numero, float):
            numero = int(numero)
        if numero == 1:
            return 1
        elif numero > 1:
            return numero * self.__factorial(numero - 1)
        else:
            return "Valor Invalido"



# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:
from funciones import *
lista = [2, 3, 4]
funciones = Funciones(lista)
funciones.conversion_grados("C", "F")
primos = funciones.son_primos(lista)
print("Números primos:", primos)
print(funciones.mas_repetido())
funciones.factorial()




# %%
