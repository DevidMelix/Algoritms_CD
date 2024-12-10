# Реализуйте программу, которая моделирует процесс взлома паролей пользователей, 
# хэшированных с использованием алгоритмов SHA, путем перебора популярных паролей.

import hashlib, sqlite3

def type_sha(password):
    if password == '224':
        return hashlib.sha224((password).encode()).hexdigest()
    
    elif password == '256':
        return hashlib.sha256((password).encode()).hexdigest()
    
    elif password == '384':
        return hashlib.sha384((password).encode()).hexdigest()
    
    elif password == '40':
        return hashlib.sha1((password).encode()).hexdigest()
    
    elif password == '56':
        return hashlib.sha3_224((password).encode()).hexdigest()
    
    elif password == '64':
        return hashlib.sha3_256((password).encode()).hexdigest()
    
    elif password == '128':
        return hashlib.sha3_512((password).encode()).hexdigest()


POPULATION_PASSWORD = ['1234567', '123', '12345', 'sex', 'privet', 'moscow', 'Moscow', 'Moscow2', 'russia', 
                       'secret', 'qwerty', 'password', '12345678', 'qwerty123', '1q2w3e', '1q2w3e4r', '123123' ]

con = sqlite3.connect('10afbed.db')
cur = con.cursor()
cur.execute('SELECT * FROM NERF')
users = cur.fetchall()
hack_users = []


for data in users:
    login = data[1]
    password = data[2]
    for popular_password in POPULATION_PASSWORD:
        if type_sha(len(password)) == hashlib.sha224((popular_password).encode()).hexdigest():
            hack_users.append({'login': login, 'password': popular_password})



for user in hack_users:
    print(user)
print(len(hack_users))