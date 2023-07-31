# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    resultado = 1
    if numero != int or numero < 1:
        return None
    else:
        while numero > 1:
            resultado *= numero
            numero -= 1
    return resultado

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    if type(valor) != int:
        return None
    elif valor == 1 or valor == 2 or valor == 3 or valor == 5 or valor%2!=0 and valor%3!=0 and valor%5!=0:
        return True
    else:
        return False
    return 'Funcion incompleta'
    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumplirAnios() -> debe devolver 1
        a.CumplirAnios() -> debe devolver 2
        a.CumplirAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class Animal:
        def __init__(self,especie, color):
            self.color = color
            self.especie = especie
            self.edad = 0
        def CumplirAnios(self):
            self.edad += 1
            return self.edad
    return Animal(especie,color)