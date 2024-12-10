
# фабула:
# есть база данных пользователей банка.
# создать БД клиентов банка
# ФИО
# адрес проживания
# номер карты.

# Задача:
# зашифровать номер карты с солью

# Создать процесс регистрации нового клиента, и процесс авторизации
# созданная база данных для хранения ФИО, адрес, номер карты
# пользователь через терминал вводит фио и номер карты
# система проверяет принадлежит ли эта карта этому клиенту, если нет - авторизация невозможно


import sqlite3, hashlib

connect = sqlite3.connect('bank.db')
cur = connect.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS user_bank (
    id INTEGER PRIMARY KEY,
    FIO TEXT,
    address TEXT NOT NULL, 
    card_number TEXT
    
)''')           


def get_hash_data(data):
    SOLE = 'SECRET_SOLE'
    return hashlib.sha256((data + SOLE).encode()).hexdigest()


def text_start_menu():
    print('(1) Регистрация')
    print('(2) Авторизация')
    print('(0) Выход')


def user_exit():
    print('(0) Вернуться')
    choice = input()
    if choice == '0':
        return True
    else:
        print('Введите правильную цифру!')



def registation_user():
    while True:

        fio = input('Введите свое ФИО:')
        address = input('Введите свой адрес:')
        card_number = input('Введите цифры своей банковской карты:')

        info_user = [fio, address, get_hash_data(card_number)]

        cur.execute("INSERT INTO user_bank (FIO, address, card_number) VALUES (? , ? , ?)", info_user)
        connect.commit()
    
        print('Вы успешно зарегистрировались')

        if user_exit():
            break


def check_authorization():

    while True:
        fio = input('Введите свое ФИО: ')
        cur.execute("SELECT * FROM user_bank WHERE FIO = ? ", [fio])
        result = cur.fetchall()


        if len(result) > 0:
            info = {
            'FIO': result[0][1],
            'address': result[0][2],
            'card_number': result[0][3]
            }

            print(f'Пользователь {info["FIO"]} найден!')
            card = input('Введите данные карты для авторизации: ')
            if get_hash_data(card) == info['card_number']:
                print('Вы успешно авторизовались')
                if user_exit():
                    break

            else:
                print('Вы ввели некорректный номер карты')
                if user_exit():
                    break
        else:
            print('Такого пользователя не существует')
            if user_exit():
                    break


def bank():
    while True:
        text_start_menu()
        choice = input('Введи номер: ')
        
        if choice == '0':
            break
        
        elif choice == '1':
            registation_user()

        elif choice == '2':
            check_authorization()

        else:
            print('Введите корректный номер!')


bank()


connect.close()