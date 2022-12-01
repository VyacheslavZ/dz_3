#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

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

def myFloatList(num):

    arr_list = []
    
    for i in range(num):
        rand = randint(0, 10) + round(random(), 2)
        arr_list.append(rand)
        
    return arr_list

def findSumPosition(lst):
    sum_lst = []
    print(lst)
    length = int(len(lst))

    if length % 2 == 0:
        for i in range(0, (length // 2)):
            sum_lst.append(lst[i] * lst[length - i - 1])
    else:
        length = int(len(lst) + 1)
        for i in range(0, (length // 2)):
            sum_lst.append(lst[i] * lst[length - i - 2])
    return sum_lst
print(f'Произведение = {findSumPosition(myList(inputNum("Введите число: ")))}')