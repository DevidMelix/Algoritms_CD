#лаба №1
#Написать перемещение коня по полю 20х20
#конь занимает 1 клетку
#каждый ход игрок выбирает куда он будет перемещаться.
#Возбуждать ошибку, если он перемещается в стену. !!!!!!
#перемещение возможны вверх, вниз, влево, вверх.
#    на карте есть камни, в которые нельзя так же наступать


from random import randint


#Создаем расположение начальной точки, финальной и камней
def generate_place_all(quantity_cobblestones):
    quantity_cobblestones += 2 # +2 это начальная точка и финальная
    points = []
    for _ in range(quantity_cobblestones):
        #Создаем точку словарь с координат. x y и добавляем в массив
        point = {'x': randint(1, 19), 'y': randint(1,19)}
        points.append(point)
    
    return points



def game():
    print('Выйдите ночью в поле с конём и помогите ему найти яблоко!')
    points = generate_place_all(5)

    start_player= {'x': points[0]['x'], 'y': points[0]['y']}
    final_point = {'x': points[1]['x'], 'y': points[1]['y']}
    cobblestone =points[2:] 


    while True:
        try:
            print(start_player)
            choice_player = int(input("""Выберите в каком направлению пойти коню
    1-Влево 
    2-Вправо 
    3-Вниз 
    4-Вверх
    5-Бросить коня
    Ответ: """))

            last_player = {'x': start_player['x'], 'y': start_player['y']} # Чтобы возвращать коня 

            if choice_player == 1: #Влево
                start_player['x'] -= 1
            elif choice_player == 2: #Вправо
                start_player['x'] += 1
            elif choice_player == 3: #Вниз
                start_player['y'] -= 1
            elif choice_player == 4: #Вверх
                start_player['y'] += 1
            elif choice_player == 5: #Конец игры
                print('Конь обиделся на вас')
                break


            if start_player['x'] in [0, 20] or start_player['y'] in [0, 20]:
                raise ZeroDivisionError('Вы врезались в забор, конь разочаровался в вас!')

            if any((start_player['x'] == point['x'] and start_player['y'] == point['y']) for point in cobblestone): #chatGPT
                raise Exception('Конь споткнулся об камень конь разочаровался в вас снова!')

            elif (start_player['x'], start_player['y']) == (final_point['x'], final_point['y']):
                print('Конь съел яблоко, поздравляю!')
                break
            
    

        except ValueError:
            print('Конь не умеет так!')
            continue

        except ZeroDivisionError as fence:
            print(fence)
            start_player['x'], start_player['y'] = last_player['x'], last_player['y'] #Возвращаем коня
            continue


        except Exception as cooble:
            print(cooble)
            start_player['x'], start_player['y'] = last_player['x'], last_player['y']
            continue





game()




























