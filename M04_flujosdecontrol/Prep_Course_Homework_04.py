#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

Var1= 8
if Var1<0:
    print("Este número: ",Var1," es menor que 0")
elif Var1>0:
    print("Este número: ",Var1,"es mayor que 0")
else:
    print("Este número es igual que 0")



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

Var1= 1
Var2= "Gabriel"
if type(Var1)==type(Var2):
    print("Estas variables tienen el mismo tipo de dato")
else:
    print("Estas variables tiene un tipo de dato diferente")



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for i in range(1,21):
    if i%2==0:
        print(i," Es un número par")
    else:
        print(i," Es un número impar")




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(6):
    print(i, " elevado a la potencia 3 es: ",(i**3))




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
Var1= 8
for i in range(Var1):
    print("Este texto se repetirá ", Var1," veces")




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

Var1= 8
if Var1>0:
    while Var1>0:
        i=Var1*(Var1-1)
        print(i)
        Var1-=1



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

Var1=4
while Var1 >0:
    for i in range(Var1):
        print("El número ", Var1,"Se repite por ", (i+1), " vez ")
    Var1-=1



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

Var1= 10
for i in range(Var1):
    while i%2==0:
        print("La potencia en base 2 de ", i," es: ",(i**2))
        i+=1
        



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
Var1= 30
for i in range(Var1):
    if i==2 or i==3 or i==5:
        print(i)
    else:
        while i%2!=0 and i%3!=0 and i%5!=0:
            print(i)
            i+=1



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

Var1= 30
for i in range(Var1):
    if i==2 or i==3 or i==5:
        print(i)
    else:
        while i%2!=0 and i%3!=0 and i%5!=0:
            print(i)
            break



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
Var1= 30
for i in range(Var1):
    if i==2 or i==3 or i==5:
        print(i)
    else:
        while i%2!=0 and i%3!=0 and i%5!=0:
            print(i)
            break # Ya no repite el while sino que lo finaliza, ahorrando tiempo y recursos



# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
Var1=100
Var2=300
while Var1<=Var2:
    Var1+=1
    if Var1%12==0:
        print(Var1)
    else:
        continue




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
Var1 = int(input("¿Qué número quieres buscar? "))
if Var1==2 or Var1==3 or Var1==5 or (Var1%2!=0 and Var1%3!=0 and Var1%5!=0):
    print(Var1," Es un número primo")
else:
   print(Var1," No es un número primo")
while True:
    Var2 = input("¿Quieres encontrar el número primo siguiente? S/N ")
    if Var2.lower() == 's':
        Var1 += 1
        while not (Var1==2 or Var1==3 or Var1==5 or (Var1%2!=0 and Var1%3!=0 and Var1%5!=0)):
            Var1 += 1
        print("El siguiente número primo es", Var1)
    else:
        break



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
Var1=100
Var2=300
while (Var1-1)<=Var2:
    Var1+=1
    if Var1%3==0 and Var1%6==0:
        print(Var1)
        break
    else:
        continue



# %%
