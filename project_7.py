#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

print()
print('Задание 1')
print()
class Matrix:
    def __init__(self,list_1,list_2):
        self.matr_1=list_1
        self.matr_2=list_2

    def __str__(self):
        print(f'Матрица 1: {self.matr_1}')
        print(f'Матрица 2: {self.matr_2}')
        print('Привычный вид матрицы 1:')
        #соединение элементов с помощью \n, соединение внутри с помощью 2 пробелов
        print(str('\n'.join(['  '.join([str(j) for j in i]) for i in self.matr_1])))
        print('Привычный вид матрицы 2:')
        return str('\n'.join(['  '.join([str(j) for j in i]) for i in self.matr_2]))

    def __add__(self):
        matr_zero=[[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(self.matr_1)):
            for j in range(len(self.matr_2[i])):
                matr_zero[i][j]=self.matr_1[i][j]+self.matr_2[i][j]
        print(f'Сложение двух матриц: ')
        return str('\n'.join(['  '.join([str(j) for j in i]) for i in matr_zero]))
matrix_1=Matrix([[1, 2, 3],[3,4 ,5],[5, 6 ,7]], [[11, 22, 33],[33,44,55],[55, 66 ,77]])
print(matrix_1.__str__())
print(matrix_1.__add__())
answer_1=input('Продолжить? ')

#2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#   К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
print()
print('Задание 2')
print()
class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_1(self):
        return self.width / 6.5 + 0.5

    def get_square_2(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общий расход ткани: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто: {self.square_c}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм: {self.square_j}'


coat = Coat(20, 30)
jacket = Jacket(10, 20)
print(coat)
print(coat.get_sq_full)
print()
print(jacket)
print(jacket.get_sq_full)
answer_1=input('Продолжить? ')
#3. Реализовать программу работы с органическими клетками.
#   Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
#   В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
#   Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
print()
print('Задание 3')
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Клетки: {self.quantity * "*"}'

    def __add__(self, other):
        print('Сложение: ')
        print(self.quantity + other.quantity)
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        print('Вычитание: ')
        print(self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно'))
        return Cell(self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 else print('Отрицательно')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells_1 = Cell(33)
cells_2 = Cell(9)
print()
print(cells_1)
print(cells_2)
print(cells_1 + cells_2)
print(cells_1 - cells_2)
print()
print(cells_2.make_order(5))
print(cells_1.make_order(10))
