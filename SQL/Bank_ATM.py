
# Создать четыре таблицы с клиентами банка
# Имя, баланс, логи транзакций (от кого, сколько(пришло или ушло))

# создать возможность вывода\ввод в наличные (можно обойтись без атомарности и блокировок)
# создать интерфейс переводов безналичных денег одного клиента другому, по имени
# учесть, что нельзя переводить больше чем есть на балансе.
# использовать пакеты запросов. Пакет атомарных запросов.
# Использовать блокировки таблиц



import sqlite3
from datetime import datetime
connect = sqlite3.connect('clients.db')
cur = connect.cursor()



def txt_show_atm(name):
    f'Приветствую {name}! Что сегодня будем делать?'
    '(1) Пополнить'
    '(2) Вывести'
    '(3) Перевод'
    '(4) Показать логи'



def autorizathion(value):
    # Подключаемся к базе данных
    connection = sqlite3.connect('clients.db')
    cursor = connection.cursor()

    # Получаем список всех таблиц в базе данных
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        # Формируем запрос для поиска значения в конкретной таблице
        query = f"SELECT * FROM {table_name} WHERE name=?;"
        cursor.execute(query, (value,))
        result = cursor.fetchone()


        # Если значение найдено, возвращаем название таблицы
        if result is not None:
            connection.close()
            return table_name

    connection.close()
    # Если значение не найдено, возвращаем None
    return False


def get_current_balance(table):
    connection = sqlite3.connect('clients.db')
    cursor = connection.cursor()

    # Получаем текущий баланс
    current_balance_query = f"SELECT balance FROM {table};"
    cursor.execute(current_balance_query)
    current_balance = cursor.fetchone()[0]

    connection.close()

    return current_balance




def create_log_add_money(table, money, word='Пополнено'):
    connection = sqlite3.connect('clients.db')
    cursor = connection.cursor()

    # Берем текущий лог
    current_log_query = f"SELECT log FROM {table};"
    cursor.execute(current_log_query)
    current_log = cursor.fetchone()[0]

    # Создаем новую запись в логе
    log_entry = f"{datetime.now()} - {word}: {money} руб."
    new_log = f"{current_log}\n{log_entry}"

    return new_log



def create_log_take_money(table, money, word='Снято'):
    connection = sqlite3.connect('clients.db')
    cursor = connection.cursor()

    # Берем текущий лог
    current_log_query = f"SELECT log FROM {table};"
    cursor.execute(current_log_query)
    current_log = cursor.fetchone()[0]

    # Создаем новую запись в логе
    log_entry = f"{datetime.now()} - {word}: {money} руб."
    new_log = f"{current_log}\n{log_entry}"

    return new_log



def add_money(table):
    print('Какую сумму желаете пополнить?')
    money = int(input('Сумма: '))

    if money <= 0:
        return 'На такую сумму нельзя пополнить!'
    
    connection = sqlite3.connect('clients.db')
    cursor = connection.cursor()

    # Получаем текущий баланс
    current_balance = get_current_balance(table)

    # Добавляем сумму к текущему балансу
    new_balance = current_balance + money

    #Добаваление лога
    new_log = create_log_add_money(table, money)

    # Обновляем баланс и лог
    update_query = f"UPDATE {table} SET balance=?, log=?;"
    cursor.execute(update_query, (new_balance, new_log))

    connection.commit()
    connection.close()



def take_money(table):
    connection = sqlite3.connect('clients.db')
    cursor = connection.cursor()

    # Получаем текущий баланс
    current_balance = get_current_balance(table)

    print('Какую сумму желаете снять?')
    print(f'Ваш баланс {current_balance} ')
    money = int(input('Сумма: '))

    if money > current_balance and money <= 0:
        return 'На такую сумму нельзя снять!'
    

    # Добавляем сумму к текущему балансу
    new_balance = current_balance - money

    #Добаваление лога
    new_log = create_log_take_money(table, money)

    # Обновляем баланс и лог
    update_query = f"UPDATE {table} SET balance=?, log=?;"
    cursor.execute(update_query, (new_balance, new_log))

    connection.commit()
    connection.close()


def money_transfer(give_money):
    print('Кому хотите перевести?')
    two_client = input('Напишите имя и фамилию через _')
    get_money = autorizathion(two_client)

    if get_money == False:
        return print('Такая пользователя нет!')


   

    # Получаем текущий баланс 1 клиента
    give_current_balance = get_current_balance(give_money)

    # Получаем текущий баланс 2 клиента
    gift_current_balance = get_current_balance(get_money)

    print('Какую сумму желаете снять?')
    print(f'Ваш баланс {give_current_balance} ')
    money = int(input('Сумма: '))

    if money > give_current_balance or money <= 0:
        return print('На такую сумму нельзя снять!')

    # Операция с балансами 1 и 2 клиента
    give_new_balance = give_current_balance - money
    gift_new_balance = gift_current_balance + money

    # создаем лог 1 клиента
    give_current_log = create_log_take_money(give_money, money, f'Перевод {get_money}')

    # создаем лог 2 клиента
    get_current_log = create_log_add_money(get_money, money, f'Получено от {give_money}')

    
    connection = sqlite3.connect('clients.db')
    cursor = connection.cursor()

    # Обновление лога 1 клиента
    update_query = f"UPDATE {give_money} SET balance=?, log=?;"
    cursor.execute(update_query, (give_new_balance, give_current_log))

    # Обновление лога 2 клиента
    update_query = f"UPDATE {get_money} SET balance=?, log=?;"
    cursor.execute(update_query, (gift_new_balance, get_current_log))

    

    connection.commit()
    connection.close()





def ATM():
    name = input('Введите свое имя и фамилию через _: ')
    name_table = autorizathion(name)

    if name_table == False:
        return 'Вы ввели неправильно имя пользователя либо такого пользователя нет'
    
    txt_show_atm(name)











