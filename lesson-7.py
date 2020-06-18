# author: Плуталов Максим Александрович

# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

class Matrix():
    def __init__( self, arr ):
        self.arr = arr

    # Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    def __str__( self ):
        return '\n'.join( str(s) for s in self.arr )


    # Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
    # Matrix (двух матриц). Результатом сложения должна быть новая матрица.
    def __add__( self, other ):
        return Matrix( [[j[0] + j[1] for j in zip(i[0], i[1])] for i in zip( self.arr, other.arr )] )



matrix1 = Matrix([ [31, 22],[37,43],[51,86] ])
matrix2 = Matrix([ [3, 5, 32], [2, 4, 6], [-1, 64, -8] ])
matrix3 = Matrix([ [3, 5, 8, 3], [8, 3, 7, 1] ])
matrix4 = Matrix([ [-1, -1],[0,0],[-2,-2] ])

print( 'matrix1:', matrix1, end = '\n\n', sep = '\n' )
print( 'matrix2:', matrix2, end = '\n\n', sep = '\n' )
print( 'matrix2:', matrix3, end = '\n\n', sep = '\n' )
print( 'matrix4:', matrix4, end = '\n\n', sep = '\n' )

print( 'matrix1 + matrix4:', matrix1 + matrix4, end = '\n\n', sep = '\n' )

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

from abc import ABC, abstractmethod

class Clothing(ABC):
    name = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass

class Coat(Clothing):
    name = 'пальто'

    def __init__(self, v):
        self.v = v

    def __str__(self):
        return '[' + self.name + ' размера ' + str(self.v) + ']'

    @property
    def fabric_consumption(self):
        return self.v / 6.5 + 0.5

class Suit(Clothing):
    name = 'костюм'

    def __init__(self, h):
        self.h = h

    def __str__(self):
        return '[' + self.name + ' размера ' + str(self.h) + ']'

    @property
    def fabric_consumption(self):
        return 2 * self.h + 0.3

coat = Coat( 52 )

print( coat, '; ткани надо:', coat.fabric_consumption )

suit = Suit( 48 )

print( suit, '; ткани надо:', suit.fabric_consumption )

# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).

class Cell():
    def __init__( self, size ):
        self.size = size

    def __str__( self ):
        return "Cell(size:{})".format( self.size )

    # Перегружаем оператор +
    def __add__( self, other ):
        return Cell( self.size + other.size )

    # Перегружаем оператор -
    def __sub__( self, other ):
        new_size = self.size - other.size
        if new_size > 0:
            return Cell( new_size )
        else:
            raise ArithmeticError( new_size )

    # Перегружаем оператор *
    def __mul__( self, other ):
        return Cell( self.size * other.size )

    # Перегружаем оператор /
    def __truediv__( self, other ):
        return Cell( self.size // other.size )

    # string representation
    def make_order( self, rowsize ):
        residual = self.size
        strres = ''
        while residual:
            thisrowsize = rowsize if residual >= rowsize else residual
            strres += '*' * thisrowsize
            residual -= thisrowsize
        return strres


c5 = Cell(8)
c6 = Cell(9)

print( 'add: c5 + c6:', c5 + c6 )

print( 'sub: c6 - c5:', c6 - c5 )

try:
    print( c5 - c6 )
except ArithmeticError:
    print( 'sub: c5 - c6: Wrong sub args' )

print( 'mul: c5 * c6:', c5 * c6 )

print( 'div: c5 / c6:', c5 / c6 )

print( 'div: c6 / c5:', c6 / c5 )
