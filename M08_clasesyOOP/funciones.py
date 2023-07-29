class Funciones:
    def __init__(self, listas):
        self.lista = listas

    def __es_primo(self, numero):
        if numero == 2 or numero == 3 or numero == 5:
            return True
        elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0:
            return False
        else:
            return True

    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversor(i, origen, destino), 'grados', destino)

    def son_primos(self, numeros):
        primos = []
        for i in numeros:
            if self.__es_primo(i):
                primos.append(i)
        return primos

    def mas_repetido(self):
        conteo = {}
        for x in self.lista:
            if x in conteo:
                conteo[x] += 1
            else:
                conteo[x] = 1
        valor_max = 0
        dato = 0
        for x in conteo:
            if conteo[x] >= valor_max:
                valor_max = conteo[x]
                dato = x
        return "El número más repetido es {} con {} repeticiones.".format(dato, valor_max)

    def factorial(self):
        for i in self.lista:
            print('El factorial de', i, 'es', self.__factorial(i))

    def __conversor(self, valor, origen, destino):
        x = 0
        if origen == "C" and destino == "F":
            x = (valor * (9 / 5) + 32)
        elif origen == "C" and destino == "K":
            x = valor + 273.15
        elif origen == "F" and destino == "C":
            x = (valor - 32) / (9 / 5)
        elif origen == "K" and destino == "C":
            x = valor - 273.15
        elif origen == "F" and destino == "K":
            x = (valor + 459.67) * (5 / 9)
        else:
            x = 1.8 * (valor - 273.15) + 32
        return "El resultado de la conversión es: {}".format(x)

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
            return "Valor Inválido"
