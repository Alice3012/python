#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#   В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
#   преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
#   и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

print('Задание 1')
class Data:
    def __init__(self,day_month_year):
        self.day_month_year=day_month_year

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != ' ': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        day=int(day)
        month=int(month)
        year=int(year)
        if day<32 and day>0:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Проверка пройдена'
                else:
                    return f'Неверная дата'
            else:
                return f'Неверная дата'
        else:
            return f'Неверная дата'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


data_1 = Data('15 10 2019')
print(data_1)
print()
data_2=input('Введите дату через пробелы: ').split(' ')
print(data_1.extract('15 10 2019'))
print(Data.valid(data_2[0],data_2[1],data_2[2]))
print()
answer=input('Продолжить? ')
print()

#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
#   вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
#   эту ситуацию и не завершиться с ошибкой.
print('Задание 2')
print()
class OwnError:
    def __init__(self,one,two):
        self.one = one
        self.two = two


    def divide_0(self):
        try:
            print(f'Результат деления: {float(self.one) / float(self.two)}')
        except ZeroDivisionError:
            print('Деление на ноль')

input_1 = input("Введите числитель и знаменатель через пробел: ").split(' ')
div_1=OwnError(input_1[0],input_1[1]).divide_0()
print()
answer=input('Продолжить? ')
print()

#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#   Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
#   Класс-исключение должен контролировать типы данных элементов списка.
print('Задание 3')
print()
class OwnError:
    def __init__(self):
        self.list_1=[]
    def trying(self):
        while True:
            input_1 = input("Введите содержимое списка : ")
            try:
                input_1=float(input_1)
                self.list_1.append(input_1)
                print(f'Содержимое списка: {self.list_1} \n')
            except ValueError:
                print(f'Это не число')
                print(type(input_1))
                answ=input('Дальнейший ввод элементов списка? (Введите -, если нет) ')
                if answ=='-':
                    print(f'\nОкончательный список: {self.list_1} \n')
                    return f'\nПрограмма завершена'

pr_1=OwnError()
pr_1.trying()
answer = input('Продолжить? ')
print()

#4 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
#  который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#  В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
#  уникальные для каждого типа оргтехники.
print('Задание 4')
print()
class OrgTech:

    def __init__(self,name,price,year,color):
        self.name=name
        self.price=price
        self.year=year
        self.color=color
        self.list=[]
    def __str__(self):
        return f'Наименование товара - {self.name},цена - {self.price}, год производства - {self.year}, цвет - {self.color}'

    def enter(self):
        while True:
            try:
                name_1=input('Введите наименование товара: ')
                price_1=float(input('Введите цену на товар: '))
                if price_1>0:
                    year_1=int(input('Введите год производства: '))
                    if year_1<2020 and year_1>0:
                        color_1=input('Введите цвет товара: ')
                        full_1={'Наименование': name_1,
                                'Цена на товар':price_1,
                                'Год производства':year_1,
                                'Цвет товара':color_1}
                        self.list.append(full_1)
                        print('\nТекущий список товаров')
                        for el in self.list:
                            print(el)
                    else:
                        print('Ошибка ввода данных')
                        answ = input(f'\nПродолжить выполнение программы? ( - для выхода)')
                        if answ == '-':
                            return f'\nПрограмма завершена'
                else:
                    print('Ошибка ввода данных')
                    answ = input(f'\nПродолжить выполнение программы? ( - для выхода)')
                    if answ == '-':
                        return f'\nПрограмма завершена'
                answ = input(f'\nПродолжить выполнение программы? ( - для выхода)')
                if answ == '-':
                    return f'\nПрограмма завершена'
            except ValueError:
                print('Ошибка ввода данных')
                answ=input(f'\nПродолжить выполнение программы? ( - для выхода)')
                if answ == '-':
                    return f'\nПрограмма завершена'

class Printer(OrgTech):
    def __init__(self,name,price,year,color):
        super(Printer, self).__init__(name,price,year,color)
        self.dict_p={'Наименование принтера': self.name,
                   'Цена на товар':self.price,
                   'Год производства':self.year,
                   'Цвет товара':self.color}
    def printp(self):
        return f'\nОтслежка принтера: {self.dict_p}'

class Scaner(OrgTech):
    def __init__(self,name,price,year,color):
        super(Scaner, self).__init__(name,price,year,color)
        self.dict_p={'Наименование сканера': self.name,
                   'Цена на товар':self.price,
                   'Год производства':self.year,
                   'Цвет товара':self.color}
    def printp(self):
        return f'\nОтслежка сканера: {self.dict_p}'

class Cserox(OrgTech):
    def __init__(self,name,price,year,color):
        super(Cserox, self).__init__(name,price,year,color)
        self.dict_p={'Наименование ксерокса': self.name,
                   'Цена на товар':self.price,
                   'Год производства':self.year,
                   'Цвет товара':self.color}
    def printp(self):
        return f'\nОтслежка ксерокса: {self.dict_p}'


print_1=Printer('Принтер ',10000,1990,'синий')
scan_1=Scaner('Сканер ',15000,1996,'синий')
cser_1=Cserox('Ксерокс ',10000,1994,'синий')

print('\nПРИНТЕРЫ')
print_1.enter()
print('\nСКАНЕРЫ')
scan_1.enter()
print('\nКСЕРОКСЫ')
cser_1.enter()
answer = input('Продолжить? ')
print()

#7 Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
#  методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
#  и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
print('Задание 7')
print()
class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.a = num_1
        self.b = num_2

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'

z_1=input('Введите действительную и комплексную часть первого числа через пробел ').split(' ')
z_2=input('Введите действительную и комплексную часть второго числа через пробел ').split(' ')
c_1 = ComplexNumber(int(z_1[0]), int(z_1[1]))
c_2 = ComplexNumber(int(z_2[0]), int(z_2[1]))
print(c_1 + c_2)
print(c_1 * c_2)

