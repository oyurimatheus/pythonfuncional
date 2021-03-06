class Gasto:

    def __init__(self, categoria, valor):
        self.__categoria = categoria
        self.__valor = valor

    @property
    def categoria(self):
        return self.__categoria

    @property
    def valor(self):
        return self.__valor

    @staticmethod
    def de_tupla(tupla):
        categoria, valor = tupla
        return Gasto(categoria, valor)
