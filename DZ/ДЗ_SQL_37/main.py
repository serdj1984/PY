""" ----------------------------------------------------------------- #
# ЗАДАНИЕ                                                             #
# Реализовать интерфейс для регистрации,                              #
# редактирование и удаления записей о продавцах и заказчиков.         #
# Создать таблицы по их описанию                                      #
#                                                                     #
#       для Salespeople:                                              #
# id(уникальный номер продавца)                                       #
# sname (имя)                                                         #
# city (город)                                                        #
# comm (комиссионные)                                                 #
#                                                                     #
# для Customers:                                                      #
# id(уникальный номер заказчика)                                      #
# cname (имя)                                                         #
# city (город)                                                        #
# rating (рейтинг)                                                    #
# id_sp(номер продавца, который обслуживает этого заказчика)          #
# ------------------------------------------------------------------- #"""

from sqlite3 import *
import sqlite3 as sql
import random as r

def cur_(x):
    return cur.execute(f'SELECT * FROM users WHERE name_user = "{x}";')

def update_s(n,b):
        if n == 's_name':
            cur.execute(f"""UPDATE `salespeople` SET 
                        `s_name`='{b}' WHERE 1""")
        if n == 'city':
            cur.execute(f"""UPDATE `salespeople` SET 
                        `city`='{b}' WHERE 1""")
        if n == 'comm':
            cur.execute(f"""UPDATE `salespeople` SET 
                        `comm`='{b}' WHERE 1""")
def update_c(n,b):
        if n == 'c_name':
            cur.execute(f"""UPDATE `customers` SET 
                        `c_name`='{b}' WHERE 1""")
        if n == 'city':
            cur.execute(f"""UPDATE `customers` SET 
                        `city`='{b}' WHERE 1""")
        if n == 'rating':
            cur.execute(f"""UPDATE `customers` SET 
                        `comm`='{b}' WHERE 1""")
def delete_c(n):
    cur.execute(f"""DELETE FROM customers WHERE `customers`.`c_name` = {n}""")

with sql.connect("btn.db") as con:
    cur = con.cursor()

# создаем таблицу с пользователями   
    cur.executescript("""
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_user VARCHAR(50) UNIQUE NOT NULL, 
                password TEXT NOT NULL);
                """)
# создаем таблицу с продавцами
    cur.executescript("""
                CREATE TABLE IF NOT EXISTS salespeople(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                s_name VARCHAR(50) NOT NULL, 
                city VARCHAR(50) NOT NULL,
                comm INTEGER NOT NULL,
                id_user INTEGER NOT NULL,
                FOREIGN KEY (id_user) REFERENCES users(id));
                """)  
# создаем таблицу с заказчиками    
    cur.executescript("""
                CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                c_name VARCHAR(50) NOT NULL, 
                city VARCHAR(50) NOT NULL,
                rating INTEGER NOT NULL,
                id_sp INTEGER,
                id_user INTEGER NOT NULL,
                FOREIGN KEY (id_user) REFERENCES users(id));
                """) 

    # создали админа -  просто так
    cur.execute("""
                 INSERT INTO users (name_user, password) VALUES ("admin", "admin1234")
                 """)
    
    # Авторизация пользователей
    name_user = 'Roma' # input('введите логин - ') 
    password = 'Roma123' # input('введите пароль - ')
    cur_(name_user) # ставим курсор на имя пользователя
    res_name = cur.fetchall()
    print(res_name)
    if res_name[0][1] == name_user and res_name[0][2] == password:
        print('Вы успешно авторезированы')
    else:
        print('Не верный логин или пороль')

    # Регистрация пользователей
    name_user = 'Roma' # input('введите логин - ') 
    password = 'Roma1234' # input('введите пароль - ')
    cur_(name_user) # ставим курсор на имя пользователя
    res_name = cur.fetchall()
    if res_name != []:
        print('Имя пользователя уже используется')
    elif res_name == []:
        cur.execute(f'INSERT INTO users (name_user, password) VALUES ("{name_user}", "{password}")')
    cur_(name_user) # ставим курсор на имя пользователя
    res_name = cur.fetchall()
    print(res_name)
    in_ = '2' # input("""Вы продовец введите 1 Вы заказчик введите 2 - """)
    if in_ == '1':
        s_name, city, comm = 'Иван', 'Москва', r.randint(0,30)
        cur.execute(f'INSERT INTO salespeople (s_name, city, comm, id_user) VALUES ("{s_name}", "{city}",{comm},{res_name[0][0]})')
        print('Вы успешно зарегистрировались')
    if in_ == '2':
        s_name, city,  = 'Рома', 'Химки'
        cur.execute(f'INSERT INTO customers (c_name, city, rating, id_user) VALUES ("{s_name}", "{city}",0,{res_name[0][0]})')
        print('Вы успешно зарегистрировались')

    # Редактирование и удаление записей о продовцах и заказчиках
    cur_(name_user) # ставим курсор на имя пользователя
    res_name = cur.fetchall()
    id_user = res_name[0][0]
    cur.execute(f'SELECT * FROM customers WHERE id_user = "{id_user}";')
    res_name = cur.fetchall()
    _in = 'c_name'
    c_name = 'Кирил'
    city = 'Подольск'
    rating = 25
    update_c(_in, c_name)
    delete_c(c_name)
    


    result = cur.execute(""" SELECT * FROM users;""")
    for row in result.fetchall(): 
        print(row) 

    result = cur.execute(""" SELECT * FROM salespeople;""")
    for row in result.fetchall(): 
        print(row)

    result = cur.execute(""" SELECT * FROM customers;""")
    for row in result.fetchall(): 
        print(row) 

    
   