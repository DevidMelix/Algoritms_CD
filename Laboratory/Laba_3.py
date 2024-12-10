# Реализовать систему управления складами с использованием принципа LIFO (последний пришел — первый ушел). 
# Задача — написать функции для добавления, удаления и перемещения контейнеров между складами, 
# а также для получения информации о содержимом склада. 
# Функции должны учитывать ограничения по высоте склада и предоставлять соответствующие сообщения в случае нарушения правил.


#def add_parametr_storages():
#    parametrs_storage = [
##          name            container         height_storage
#        ['Москва', [2, 5, 2, 1, 52, 25] ,        3             ],
#        ['Лобня',   [2, 4, 22, 1, 2, 4, 5],      1             ],
#        ['Екатербург', [2, 1, 5, 2, 5, 3],       1             ],
#        ['Домодедово', []                ,       1             ]
#    ]
#    
#    storages = []
#    for parametrs in parametrs_storage:
#            storages.append({
#                parametrs[0]: parametrs[1],
#                'height_storage': parametrs[2],
#                'height_container': parametrs[3]
#            })
#    
#    return storages


storages = []


def add_storage(name_storage, height_storage):
    storages.append(
        {f'{name_storage}': {
        'storages': [],
        'height_storage': height_storage
        },
            })
    

def delete_storage(name):
    for storage in storages:
        if name in storage:

            if storage[name]['storage'] == []:
                storages.remove(storage)
                break

            else:
                print('Нельзя удалить склад в нем что-то есть!')
                break
        

def set_lifo(name, data, height_container):
    for storage in storages:
        if name in storage:
            if height_container <= storage[name]['height_storage']:
                storage[name]['storages'].append({'№':data, 'height': height_container})
                break

            else:
                return False


def get_lifo(name, amount):
    for storage in storages:
        if name in storage:

            fifo = storage[name]['storage']
            last = fifo[-amount:]
            del fifo[-amount:]

            return last


def info_lifo(name, number):
    for storage in storages:
        if name in storage:
            
            return storage[name]['storage'][-number:]


def moving_lifo(name1, name2, amount):
    two_index_storage = find_index_two_storage(name1, name2)
    
    for _ in range(amount):
        last =  storages[int(two_index_storage[1])][name1]['storage'].pop()
        storages[int(two_index_storage[2])][name2]['storage'].append(last)


def find_index_two_storage(name1, name2):
    two_storage = ['empty']

    for i, storage in enumerate(storages):
        if name1 in storage:
            two_storage.append(str(i))
    
    for i, storage in enumerate(storages):
        if name2 in storage:
            two_storage.append(str(i))
            
    return two_storage


add_storage('Москва', 3)
add_storage('Лобня', 2)

set_lifo('Москва', 142, 2)
set_lifo('Москва', 1, 2)
set_lifo('Москва', 4, 3)

set_lifo('Лобня', 3, 2)
set_lifo('Лобня', 5, 2)
set_lifo('Лобня', 6, 3)
print(storages)
