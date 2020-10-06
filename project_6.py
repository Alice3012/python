#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#   Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#   Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#   Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
#   Проверить работу примера, создав экземпляр и вызвав описанный метод.

print()
print('Задание 1')
print()

import time
class TrafficLight:
    #атрибут класса
    __colors=['Красный', 'Желтый', 'Зеленый']

    def running(self):
        print(self.__colors[0])
        time.sleep(7)
        print(self.__colors[1])
        time.sleep(2)
        print(self.__colors[2])
        time.sleep(5)

Traf_1 = TrafficLight()
Traf_1.running()
answer_1=input('Продолжить? ')

#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#   Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
#   Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#   Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
#   Проверить работу метода.
print()
print('Задание 2')
print()
class Road:
    def __init__(self,length=None,width=None):
        self._length=length if length else 'Не задана длина'
        self._width=width if width else 'Не задана ширина'

    def method(self):
        if self._width!='Не задана ширина' and self._length!='Не задана длина':
            result_1=self._length*100*self._width*100*5*2.69
            print(f'Масса асфальта (длина * ширина * высота * плотность асфальта): {self._length}м * {self._width}м * 5см * 2,59 г/см^3 = {result_1/1000000} тонн')
        else:
            'Невозможно определить массу без параметров'

road_1=Road(1000,10)
road_1.method()
answer_1=input('Продолжить? ')


#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
#   Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#   Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#   Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
print()
print('Задание 3')
print()
class Worker:
    def __init__(self,name,surname,position,profit,bonus):
        self.name=name
        self.surname=surname
        self.position=position
        self._income={"Оклад": profit,'Премия':bonus}

#дочерний объект
class Position(Worker):
    def __init__(self,name,surname,position,profit,bonus):
        super(Position, self).__init__(name,surname,position,profit,bonus)
    def get_full_name(self):
        return self.name+' '+self.surname
    def get_total_income(self):
        return self._income['Оклад']+self._income['Премия']

man=Position('Василий', 'Петров', 'Работник службы безопасности', 10000,1000)
print('Полное имя сотрудника:', man.get_full_name())
print('Доход с учетом премии:', man.get_total_income())
answer_1=input('Продолжить? ')

#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#   А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#   Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#   Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
print()
print('Задание 4')
print()

class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police

    def go(self):
        print('Машина начала движение')
    def stop(self):
        print("Машина остановилась")
    def turn(self,direction):
        print('Машина повернула: ',direction)
    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
        print(f'Городская машина: {self.name}, цвет - {self.color}, полицейская - {self.is_police}, скорость в данный момент - {self.speed}')
        if self.speed>60:
            print('Превышение скорости')
        print()
class SportCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
        print(f'Спортивная машина: {self.name}, цвет - {self.color}, полицейская - {self.is_police}, скорость в данный момент - {self.speed}')

        print()
class WorkCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
        print(f'Рабочая машина: {self.name}, цвет - {self.color}, полицейская - {self.is_police}, скорость в данный момент - {self.speed}')
        if self.speed>40:
            print('Превышение скорости')

        print()
class PoliceCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
        print(f'Полицейская машина: {self.name}, цвет - {self.color}, полицейская - {self.is_police}, скорость в данный момент - {self.speed}')
        print()

town_1=TownCar(60,'black','Ford', False)
sport_1 = SportCar(180,'yellow','Ford Mustang', False)
work_1 = WorkCar(60,'white','Lada', False)
police = PoliceCar(100,'red','Ford', True)
print(f'Пример спортивной машины: {sport_1.name}, цвет - {sport_1.color}, полицейская - {sport_1.is_police}')
answer_1=input('Продолжить? ')


#5. Реализовать класс Stationery (канцелярская принадлежность).
#   Определить в нем атрибут title (название) и метод draw (отрисовка).
#   Метод выводит сообщение “Запуск отрисовки.”
#   Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#   В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
#   Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
print()
print('Задание 5')
print()
class Stationery:
    def __init__(self,title):
        self.title=title

    def draw(self):
        print('Запуск отрисовки')

class Pencil(Stationery):
    def __init__(self,title):
        super(Pencil, self).__init__(title)
    def draw(self):
        print('Запуск отрисовки карандаша',self.title)

class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)
    def draw(self):
        print('Запуск отрисовки ручки',self.title)
class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)
    def draw(self):
        print('Запуск отрисовки маркера',self.title)

my_pen = Pen('Перьевая')
my_pencil = Pencil('Механический')
my_handle = Handle('Красный')

my_pen.draw()
my_pencil.draw()
my_handle.draw()