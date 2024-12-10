
# Лаба N n
# Написать игру
# сражение с монстром. Минимум с двумя
# механика битвы следующая.
# каждый ход вы выбираете что будете защищать голову, туловище, или ноги(подпрыгиваете).
# Монстр делает тоже самое рандомно
# затем вы выбираете куда будете бить голова, туловище, ноги
# Монстр делает тоже самое рандомно
# сценарий игры на ваше усмотрение

import random

def txt_player():
    return """1 - Голова
2 - Туловище
3 - Ноги"""
    

def mechanic(action):

    if action == 1:
        return "Голова"

    elif action == 2:
        return "Туловище"
    
    elif action == 3:
        return "Ноги"


def player_stats():
    hp_player = 3

    return hp_player


def monstr_stats():
    hp_monstr = 3

    return hp_monstr


def player_state(action):

    body_part = mechanic(action)

    return body_part


def monstr_state():
    actions = [1, 2, 3]

    action_monstr = random.choice(actions)

    body_part = mechanic(action_monstr)

    return body_part


def gameplay(player_action, monstr_action):
    if player_action == monstr_action:
        return True
    else:
        return False




def game():
    print(txt_player())
    hp_player = player_stats()
    hp_monstr = monstr_stats()
    fase = 'attack'
    
    while True:
    
        action = int(input())
        
        body_part_player = player_state(action)
        body_part_monstr = monstr_state()
        
        if fase == 'attack':
        
            print(f"Вы бьете по {body_part_player}")
            if gameplay(body_part_player, body_part_monstr) == False:
            
                print("Вы попали!")
                print(f"Монстр защитил {body_part_monstr}")
    
                hp_monstr -= 1
                fase = 'defense'
                
            else:
                print("Монстр защитился!")
                fase = 'defense'
    
        elif fase == 'defense':
             
             if gameplay(body_part_player, body_part_monstr) == False:
                print("Монстр попал!")
                print(f"Монстр бил {body_part_monstr}")
                hp_player -= 1
                fase = 'attack'
             else:
                print("Монстр не попал")
                fase = 'attack'
    
        print(f'хп игрока {hp_player}')
        print(f'хп монстра {hp_monstr}')
    
        if hp_monstr == 0:
            return "Вы выиграли!"
            
        elif hp_player == 0:
            return "Вы проиграли!"
            


print(game())