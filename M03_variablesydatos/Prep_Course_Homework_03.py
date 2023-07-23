#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

x = 10
print(x)

# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:


type(8.5)


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:


type(x)


# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre= "Néstor Valbuena"


# 5) Crear una variable que contenga un número complejo

# In[3]:


complejo=1j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


type(complejo)


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


Pi= round(3.14158,4)


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

Var1= 'True'
Var2= True# NO, 'True' es un string y True es un booleano.


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(Var1))
print(type(Var2))


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:


Var3= 1+2.5


# 11) Realizar una operación de suma de números complejos

# In[2]:


Var4= 3j+1j


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

Var5=  3j +7



# 13) Realizar una operación de multiplicación

# In[5]:


15*56


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

2**8


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

Var6= 27/4
print(Var6)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:


Var7=int(Var6)
print(Var7)

# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

Var8=27%4
print(Var8)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:


Var7*4+Var8


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:


Var9= "NS2"
Var10= "NS12sd"
print(Var9+Var10)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:


Var11="2"==2
print(Var11)# Porque '2' es un string y 2 es un int y se estan comparando si son el mismo tipo de datos

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

Var12= not bool(Var11)
print(Var12)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:


a = float(3.8)# Los números decimales en python se escriben sin '' y con punto en vez de coma.


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

Var13= 3
Var13-= 1
print(Var13)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1<<2# significa que el 1 se corre 2 casillas osea 0100 en vinario que es igual a 2**2= 4



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:


2+int('2') # No se puede sumar un int con un string por lo que siempre va a dar error



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

3*"Hola "

