#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#   Об окончании ввода данных свидетельствует пустая строка.

print('')
print('Задание 1')
print('')
file_1=open('project_5_file.txt', 'w')
answer_1=True
while answer_1==True:
    answer_f=input('Введите строки для записи в файл (для окочания ввести пустую строку): ')
    if answer_f!='':
        file_1.write(f'{answer_f}\n')
    else:
        answer_1=False
        print('Ввод данных завершен')
file_1.close

file_1=open('project_5_file.txt', 'r')
print('Содержимое файла:')
line_1=file_1.read()
print(line_1)
print('')
file_1.close
answer_1=input('Продолжить?')

#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
print('')
print('Задание 2')
print('')

file_1=open('project_5_test_2.txt', 'r')
print('Содержимое файла:')
line_1=file_1.read()
print(line_1)
print('')
file_1.close()

num=0
for line_1 in open('project_5_test_2.txt','r'):
    num+=1
    #удаляю ненужные пробелы во обе стороны
    line_1 = line_1.strip(' ')
    #делю строку по пробелам
    line_2 = line_1.split(' ')
    print(f'В строке {num} количество слов - {len(line_2)}')
print(f'Количество строк в файле: {num}')
answer_1=input('Продолжить?')
#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#   Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#   Выполнить подсчет средней величины дохода сотрудников.
print('')
print('Задание 3')
print('')
num=0
sum_all=0
members_min_20=[]
for line_1 in open('staff_member.txt','r'):
    #количество сотрудников
    num += 1
    # удаляю ненужные пробелы во обе стороны
    line_1 = line_1.strip(' ')
    # делю строку по пробелам
    line_2 = line_1.split(' ')

    sum_all+=float(line_2[1])

    if float(line_2[1])<20000:
        members_min_20.append(line_2[0])
print('Средняя величина дохода сотрудников равна {:.3f}'.format(float(sum_all)/float(num)))
print(f'Работники с окладом менее 20000: {members_min_20}')
answer_1=input('Продолжить?')
#4. Создать (не программно) текстовый файл со следующим содержимым:One — 1 Two — 2 Three — 3 Four — 4
#   Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#   При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
print('')
print('Задание 4')
print('')

file_1=open('file_test_4.txt','r')
file_2=open('file_test_4_new.txt','w')
line_2_all=[]
i=1
numbers_1=['Один', 'Два','Три','Четыре']
for line_1 in file_1:
    line_2=line_1.split(' - ')
    if i == 1:
        line_2[0]=numbers_1[i-1]
        line_2_all.append(line_2[0])
        i+=1
    elif i == 2:
        line_2[0] = numbers_1[i-1]
        line_2_all.append(line_2[0])
        i+=1
    elif i == 3:
        line_2[0] = numbers_1[i-1]
        line_2_all.append(line_2[0])
        i+=1
    else:
        line_2[0] = numbers_1[i-1]
        line_2_all.append(line_2[0])

for i in range(0,4):
    str_new=line_2_all[i]+' - '+str(i+1)
    file_2.write(str_new+'\n')
print('Запись в новый файл завершена')
file_1.close()
file_2.close()
answer_1=input('Продолжить?')
#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#   Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
print('')
print('Задание 5')
print('')

file_1=open('file_test_5.txt','w')
str_1='50 '+'0.1 '+'1987 '+'115.2 '+'45 '
print(f'Пусть есть строка чисел: {str_1}')
file_1.write(str_1)
file_1.close()

sum_1=0
for line_1 in open('file_test_5.txt','r'):
    line_1=line_1.strip(' ')
    line_2=line_1.split(' ')
for i in line_2:
    sum_1+=float(i)
print('Сумма чисел в этой строке, записанной в файл, равна {:.2f}'.format(sum_1))
print('Продолжить?')
#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
#   Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#   Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
print('')
print('Задание 6')
print('')

file_1=open('file_test_6.txt','r', encoding='utf8')
print('Содержимое файла:')
line_0=file_1.read()
print(line_0)
print('')

file_1=open('file_test_6.txt','r', encoding='utf8')
for line_1 in file_1:
    sum_1 = 0
    line_2 = line_1.split(' ')
    for i in range(1,len(line_2)):
        sum_1+=float(line_2[i])
    print(f'Общее кол-во часов по предмету {line_2[0]} - {sum_1}')
file_1.close()
answer_1=input('Продолжить?')
#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#   Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#   Если фирма получила убытки, в расчет средней прибыли ее не включать.
#   Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#   Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#   Итоговый список сохранить в виде json-объекта в соответствующий файл.
print('')
print('Задание 7')
print('')
file_1=open('file_test_7.txt','r', encoding='utf8')
average_profit=0
num_1=0
list_firm=[]
list_dict={}
list_dict_avg={}
for line_1 in file_1:
    line_2=line_1.split(' ')
    firm_1=line_2[0]
    form_1=line_2[1]
    revenues_1=line_2[2]
    cost_1=line_2[3]
    profit_1=float(revenues_1)-float(cost_1)

    if profit_1>0:
        print(f'Прибыль {firm_1} равна {profit_1}')
        num_1+=1
        average_profit+=profit_1
    else:
        print(f'Убытки {firm_1} равны {abs(profit_1)}')

    list_dict[firm_1]=profit_1

print()
if average_profit>0:
    print(f'Средняя прибыль: {average_profit/num_1}')
else:
    print('Везде убытки')

print()
list_dict_avg['Средняя прибыль']=average_profit/num_1
list_firm=[list_dict,list_dict_avg]
print(list_firm)
file_1.close

import json
with open('file_test_7_new.json','w',encoding='utf8') as file_2:
    json.dump(list_firm,file_2)
print('Запись в файл json завершена')