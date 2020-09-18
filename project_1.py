#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""
a=15
b=10
print("a=",a,",","b=",b)
print("a+b=",a+b,",","a-b=",a-b,",","a*b=",a*b,",","a/b=",a/b,",","a^b=",a**b)

number_one=input("Enter smth integer: ")
number_one=int(number_one)
print("You entered '{:d}'".format(number_one))

number_two=input("Enter smth float: ")
number_two=float(number_two)
print("You entered '{:.3f}'".format(number_two))

string_one=input("Enter a string: ")
print("You entered "+string_one)
"""


#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
time_1=input("Input time in sec: ")
time_1=int(time_1)
#Всего в 1 дне 86400 секунд, 1 час = 3600сек
time_day_sec=24*60*60
if time_1>time_day_sec:
    day_1=time_1//time_day_sec
    time_12=time_1%time_day_sec
    print("Days passed ",str(day_1))

hour_1=time_1//3600
minute_1=(time_1%3600)//60
sec_1=(time_1%3600)%60
print("Time: {:02d}:{:02d}:{:02d}".format(hour_1,minute_1,sec_1))
"""

#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
num_n=input("Input n: ")
num_nn=num_n+num_n
num_nnn=num_nn+num_n
result_n=int(num_n)+int(num_nn)+int(num_nnn)
print("Sum {:d}+{:d}+{:d}={:d}".format(int(num_n),int(num_nn),int(num_nnn),result_n))
"""

#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""
num_1=input("Input positive integer: ")
num_max=0
for i in range(len(num_1)):
    if int(num_1[i])>int(num_max):
        num_max=num_1[i]
print(str(num_max))
"""

#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue_1=input("Input revenue")