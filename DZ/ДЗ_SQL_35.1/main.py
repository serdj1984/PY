"""
ЗАДАНИЕ
Создать таблицы  по их описанию
/*— для Salespeople
id(уникальный номер продавца)
sname (имя)
city (город)
comm (комиссионные)

— для Customers
id(уникальный номер заказчика)
cname (имя)
city (город)
rating (рейтинг)
id_sp(номер продавца, который обслуживает этого заказчика)*/

и вставить в них данные из файлов
customers.txt
salespeople.txt
"""
from sqlite3 import *
import sqlite3 as sql

def fun(x):
    x = x.split(',')
    x[-1] = x[-1].strip()
    b =[]
    for i in x:
        if [s for s in i if s in ' ']: i = i.strip(' ')
        if [s for s in i if s in '1234567890']: i = int(i)
        b.append(i)  
    return tuple(b)

with open("customers.txt","r", encoding='utf-8') as f:
        cus_file = f.readlines() 
        customers = []
        for line1 in cus_file:
                customers.append(fun(line1))

with open("salespeople.txt","r", encoding='utf-8') as f:
        sal_file = f.readlines()
        salespeople = []
        for line2 in sal_file:
                salespeople.append(fun(line2))
        
with sql.connect("btn.db") as con:
    cur = con.cursor()
    cur.executescript("""
                CREATE TABLE IF NOT EXISTS salespeople(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                s_name VARCHAR(50) NOT NULL, 
                city VARCHAR(50) NOT NULL,
                comm INTEGER NOT NULL);
                """)  
    
    cur.executescript("""
                CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                c_name VARCHAR(50) NOT NULL, 
                city VARCHAR(50) NOT NULL,
                rating INTEGER NOT NULL,
                id_sp INTEGER NOT NULL);
                """)  
    # for l in salespeople:
    #     cur.execute(f"""
    #                 INSERT INTO `salespeople`(`s_name`, `city`, `comm`) VALUES {l};
    #             """)
    # for n in customers:
    #     cur.execute(f"""
    #                 INSERT INTO `customers`(`c_name`, `city`, `rating`, `id_sp`) VALUES {n};
    #             """)
    
    print("""
     ●	показываем таблицу с заказчиками
-------------------------------------------------------------""")
    result = cur.execute("""
                SELECT * FROM `customers` WHERE 1;
                """)
    for row in result.fetchall():
        print(row)
    
    print("""
     ●  показываем таблицу с продавцами
----------------------------------------------------------------------""")
    result = cur.execute("""
                SELECT * FROM `salespeople` WHERE 1;
                """)
    for row in result.fetchall():
        print(row)