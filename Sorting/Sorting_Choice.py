# Лабораторная работа!
# Написать функцию которая на входе получает массив из R элементов.
# Применить к нему метод сортировки выбором
# вывесли получившейся массив


data = [10, 2, 2, 8, 5, 61, 7, 6, 9, 1]

lenght = len(data)


def selection_sort(list):
    for _ in range(lenght):

        flag = True
        for i in range(lenght-1):
            
            if data[i] > data[i+1]:
                mn = data.index(min(data[i:]))    #[START:STOP:STEP]
                data[i], data[mn] = data[mn], data[i]
                flag = False

        if flag:
            return print(data)

selection_sort(data)
            

