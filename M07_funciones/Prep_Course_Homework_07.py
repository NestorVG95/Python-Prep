#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:
def es_primo(numero):
    if numero==2 or numero==3 or numero==5:
        return(True)
    elif numero%2==0 or numero%3==0 or numero%5==0 :
        return(False)
    else:
        return(True)
es_primo(22)




# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
def son_primos(numeros):
    primos= []
    for i in numeros:
        if es_primo(i):
            primos.append(i)
    return primos
Lista1= [1,2,3,4,5,6,7,8,9,10]
primos= son_primos(Lista1)
print(primos)



# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
def mas_repetido(i):
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
            
            
Lista2= [1,2,3,4,5,6,7,8,9,10,11,12,3,3,2,2,1,54,1,2,2,3,4,5]
mas_repetido(Lista2)




# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def Conversor(valor,origen,destino):
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
Origen = input("Tu valor esta en 'C'Celcius, 'K'kelvin o 'F'Farenheit?")
Destino = input("Necesitas transformarlo en 'C'Celcius, 'K'kelvin o 'F'Farenheit?")
Valor = float(input("Ingresa tu valor a transformar"))
Conversor(Valor,Origen,Destino)


# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:
Prueba= [0,"K","C"],[0,"C","K"],[0,"C","F"],[0,"F","K"],[0,"F","C"],[0,"K","F"]
for i in Prueba:
    print(Conversor(*i))



# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
numero_factorial = int(input("Ingresa el número al que le quieres sacar su número factorial: "))
if numero_factorial < 0:
    numero_factorial = -numero_factorial
factorial(numero_factorial)



# %%
