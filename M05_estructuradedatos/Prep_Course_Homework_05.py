#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
Var1= ["Bucaramanga","Medellin","Cali","Barranquilla","Cartagena","Sogamoso","Bogotá"]
print(Var1)



# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(Var1[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print(Var1[1:4])



# 4) Visualizar el tipo de dato de la lista

# In[12]:

type(Var1)



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print(Var1[2:])



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

print(Var1[:4])

    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

Var1.append("Medellin") #Aparentemente todo esta bien
Var1.append("Buenaventura")
print(Var1)







# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:
Var1.insert(4,"San Gil")
print(Var1)




# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:

Var2 = ["Tunja","Pasto","Rio Negro","Tokio"]
Var1.extend(Var2)
print(Var1)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

Var1.index("Medellin") # Solo aparece el primer resultado de la busqueda



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:


Var1.index("San Martin") # Da error porque el valor no existe en la lista y por tanto no tiene indice


# 12) Eliminar un elemento de la lista

# In[25]:

Var1.remove("Cali")
print(Var1)



# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

Var1.remove("San Andres") #Genera error no puede ejecutar algo que no existe



# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

Var3 = Var1.pop(-1)
print(Var3)



# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(Var1*4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

Var4 = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
print(Var4)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(Var4[9:15])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

print(20 in Var4)
print(30 in Var4)



# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

Var5= "Paris"
if Var5 in Var1:
    print("La lista ya contenía a ", Var5)
else:
    Var1.append(Var5)
    print(Var5," No estaba en la lista y fué añadido")
print(Var1)



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

print(Var4.count(4))
print(Var1.count("Bucaramanga"))



# 21) Convertir la tupla en una lista

# In[52]:

Var6 = list(Var4)
print(Var6)



# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:

Var7= Var4[0]
Var8= Var4[1]
Var9= Var4[2]
print(Var7,Var8,Var9)



# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:

Var10 = {"ciudad":Var1,"Pais":["Colombia","Francia","Japon"],"Continente": ["Europa", "America", "Asia"]}




# 24) Imprimir las claves del diccionario

# In[59]:

Var10.keys()


# 25) Imprimir las ciudades a través de su clave

# In[61]:
print(Var10["ciudad"])




# %%
