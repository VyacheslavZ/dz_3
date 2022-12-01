#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint, random

def inputNum(inputText):
    flag = False
    while not flag:
        try:
            number = int(input(f"{inputText}"))
            flag = True
        except ValueError:
            print("Это не число!")
    return number

def myList(num):
    
    arr_list = []
    
    for i in range(num):
        rand = randint(0, 10)
        arr_list.append(rand)
        
    return arr_list
def findPosition(lst):
    sum = 0
    print(lst)
    for i in range(1, len(lst), 2):
        sum += lst[i]
    return sum

print(f'Сумма чисел на нечетных позициях = {findPosition(myList(inputNum("Введите число: ")))}')