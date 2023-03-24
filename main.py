'''
from abc import ABC, abstractmethod

class bancodedados(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def desconectar(self):
        pass

    @abstractmethod
    def consultar(self, consulta):
        pass

    @abstractmethod
    def atualizar(self, atualizacao):
        pass

class MySQL(bancodedados):
    def conectar(self):
        print("Conectando ao banco de dados MySQL...")

    def desconectar(self):
        print(f"Desconectando do banco de dados MySQL: {consulta}")

    def consultar(self, consulta):
        print(f"Consultando no banco de dados MYSQL...")

    def atualizar(self, atualizacao):
        print(f"Atualizando o BD MySQL: {atualizacao}")


if __name__ == '__main__':
    obj_bd = MySQL()
    obj_bd.conectar()
    obj_bd.consultar("SELECT * FROM tabea")
    obj_bd.atualizar("Tabela atualizad, coluna = valor")
    obj_bd.desconectar()



''''''
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self._lado = lado

    def lado(self):
        return self._lado

    def get_lado(self):
        return self._lado

    def set_lado(self, valor):
        self._lado = valor

    def area(self):
        vl_area = self._lado ** 2
        return vl_area

    def perimetro(self):
        vl_perimetro = 4 * self._lado
        return vl_perimetro


if __name__ == '__main__':
    obj_quad = Quadrado(3)
    print(obj_quad.area())
    obj_quad.set_lado(4)
    print(obj_quad.area())
    print('Lado:', obj_quad.get_lado())
    print('Area: ', obj_quad.area())
    print('Perimetro: ', obj_quad.perimetro())
    
    
'''''''''

from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def mostrar_mensagem(self):
        print("Esta é uma forma geométrica.")

    def mostrar_mensagem_subclasse(self):
        print("Esta é uma forma geométrica da subclasse:", self.__class__.__name__)


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, valor):
        self.lado = valor

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def get_raio(self):
        return self.raio

    def set_raio(self, valor):
        self.raio = valor

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

    def mostrar_area(self):
        print("A área do círculo é:", round(self.area(), 2))


if __name__ == '__main__':
    # Teste Quadrado
    obj_quad = Quadrado(3)
    print("Lado do quadrado:", obj_quad.get_lado())
    obj_quad.set_lado(4)
    print("Lado do quadrado:", obj_quad.get_lado())
    print("Área do quadrado:", obj_quad.area())
    print("Perímetro do quadrado:", obj_quad.perimetro())

    # Teste Circulo
    obj_circ = Circulo(5)
    print("Raio do círculo:", obj_circ.get_raio())
    obj_circ.set_raio(6)
    print("Raio do círculo:", obj_circ.get_raio())
    print("Área do círculo:", obj_circ.area())
    print("Perímetro do círculo:", obj_circ.perimetro())
    obj_circ.mostrar_area()

    # Teste mostrar mensagem
    obj_quad.mostrar_mensagem()
    obj_circ.mostrar_mensagem()
    obj_quad.mostrar_mensagem_subclasse()
    obj_circ.mostrar_mensagem_subclasse()

