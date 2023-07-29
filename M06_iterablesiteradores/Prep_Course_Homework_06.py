#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
Lista1=[]
x=-15
while x<0:
    Lista1.append(x)
    x+=1
print(Lista1)




# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
x=0
while x<len(Lista1):
    if Lista1[x]%2==0:
        print(Lista1[x])
    x+=1




# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

[x for x in Lista1 if x%2==0]



# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:
Lista2= iter(Lista1)
x=0
while x<3:
    x+=1
    print(next(Lista2))



# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
Lista3=[]
for x in enumerate(Lista1):
    Lista3.append(x)
print(Lista3)



# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
lista = [1,2,5,7,8,10,13,14,15,17,20]
faltantes = [x for x in range(1, 21) if x not in lista]
for x in faltantes:
    for i in range(len(lista)):
        if x < lista[i]:
            lista.insert(i, x)
            break
    else:
        lista.append(x)
print(lista)




# In[11]:


n = 1



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
Lista4 = [0, 1]
for i in range(2, 30):
    Lista4.append(Lista4[i-1] + Lista4[i-2])
print(Lista4)




# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

print(sum(Lista4))


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:

rango = 15 
x = rango-5
while x < rango:
    print(Lista4[x] / Lista4[x-1]) 
    x += 1 


# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i,x in enumerate(cadena):
    if x=="n":
        print(i)



# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:

Dicc1= {"clave1":"valor1","clave2":"valor2","clave3":"valor3","clave4":"valor4"}
for i in Dicc1:
    print(i)



# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:
Lista6= [i for i in cadena]
for i in Lista6:
    print(i)




# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

Lista7= [1,2,3,4,5,6,7,8,9,10,11]
Lista8= ["Blanco","Azul","Rojo","Negro","Verde"]
Lista9= zip(Lista8,Lista7)
for i in Lista9:
    print(i)



# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
Lista10= []
for i in lis:
    if i%7==0:
        Lista10.append(i)
Lista10



# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:
x= 0
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
for i in lis:
    if type(i)==list:
        x+= len(i)
    else:
        x+=1
print(x)



# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:
for i,x in enumerate(lis):
    if type(x)!=list:
        lis[i]= [x]
print(lis)



# %%
