
# Сортировка пузырьковым алгоритмом

# Написать функцию, которая на входе принимает массив из Натуральных элементов,
# На выходе получить сортированный массив на возрастание, 
# используя только метод алгоритма пузырьковой сортировки

        

test = [6,5,7,3,5,5,1,2]

lenght_list = len(test)

for len in range(lenght_list):
    flag = True
    #print(len)
    for i in range(lenght_list-1):
        if test[i] > test[i+1]:
            test[i+1], test[i] = test[i], test[i+1]
            flag = False
    if flag:
        print(test)
        break    
    

#lenght_list = len(test)
#flag = False
##c = 0
#while flag == False:
#    flag = True
#    for i in range(0, lenght_list-1):
#        if test[i] > test[i+1]:
#            test[i+1], test[i] = test[i], test[i+1]
#            flag = False
#    #c += 1
#
#print(test)
        






