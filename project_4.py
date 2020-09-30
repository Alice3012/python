#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#   В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#   Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

print()
print('Задание 1')
print()
def plata():
    try:
        time_1 = float(input('Выработка в часах: '))
        salary_1 = int(input('Ставка в у.е.: '))
        bonus_1 = int(input('Премия в у.е.: '))
        result_1 = time_1 * salary_1 + bonus_1
        print(f'Заработная плата сотрудника: {result_1}')
    except ValueError:
        return print('Not a number')
plata()
print()
answer=input('Продолжить?')
print()


#2. Представлен список чисел.
#   Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
print()
print('Задание 2')
print()
my_numbers=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список: {my_numbers}')

my_numbers_new=[]
for num_1 in range(1,len(my_numbers)):
    if my_numbers[num_1-1]<my_numbers[num_1]:
        my_numbers_new.append(my_numbers[num_1])
print(f'Результирующий список чисел: {my_numbers_new}')
print()
answer=input('Продолжить?')
print()


#3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
#   Необходимо решить задание в одну строку.
print()
print('Задание 3')
print()
print(f'Числа от 20 до 240, кратные 20 или 21: {[list_element for list_element in range(20,240) if list_element%20==0 or list_element%21==0]}')
print()
answer=input('Продолжить?')
print()


#4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
#   Сформировать итоговый массив чисел, соответствующих требованию.
#   Элементы вывести в порядке их следования в исходном списке.
#   Для выполнения задания обязательно использовать генератор.
print()
print('Задание 4')
print()
my_numbers=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Исходный список: {my_numbers}')
my_numbers_new=[list_element for list_element in my_numbers if my_numbers.count(list_element)<2]
print(f'Результирующий список чисел: {my_numbers_new}')
print()
answer=input('Продолжить?')
print()


#5. Реализовать формирование списка, используя функцию range() и возможности генератора.
#   В список должны войти четные числа от 100 до 1000 (включая границы).
#   Необходимо получить результат вычисления произведения всех элементов списка.
print()
print('Задание 5')
print()
from functools import reduce
my_numbers_new=[num_1 for num_1 in range(100,1001) if num_1%2==0]
print(f'Результирующий список чисел: {my_numbers_new}')
print(f'Результат перемножения элементов списка: {reduce(lambda x,y: x*y, my_numbers_new)}')

#6. Реализовать два небольших скрипта:
#   а) итератор, генерирующий целые числа, начиная с указанного,
#   б) итератор, повторяющий элементы некоторого списка, определенного заранее.
print()
print('Задание 6')
print()
try:
    num_a=int(input('Введите целое число, начиная с которого начать последовательность: '))
    num_b=int(input('Введите целое число, которым закончить последовательность: '))
except ValueError:
    print('   Не целое число   ')

my_numbers=[]
from itertools import count
for element_list in count(num_a,1):
    if element_list <= num_b:
        my_numbers.append(element_list)
    else:
        break
print(f'Сгенерированные целые числа: {my_numbers}')

from itertools import cycle
list_el=input('Введите элементы списка через пробел: ')
list_el=list_el.strip()
count_n=int(input('На каком элементе остановить повтор? '))
my_list=list(list_el.split(' '))
print(f'Введенный список: {my_list}')
count_i=0
repeat_list=[]
for element_list in cycle(my_list):
    if count_i<count_n:
        repeat_list.append(element_list)
        count_i+=1
    else:
        break
print(f'Список повторяющихся элементов: {repeat_list}')
print()
answer=input('Продолжить?')
print()


#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#   При вызове функции должен создаваться объект-генератор.
#   Функция должна вызываться следующим образом: for el in fact(n).
#   Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
print()
print('Задание 7')
print()
try:
    num_n = int(input('Введите число n: '))
except ValueError:
    print('Не целое число')

def func_fact(num_2):
    res_i=1
    for i in range(1,num_2+1):
        res_i=res_i*i
        yield res_i

result_n=func_fact(num_n)
i=1
print('0!=1')
while i < num_n:
    if i<=15:
        print(f'{i}!={next(result_n)}')
        i += 1
    else:
        break