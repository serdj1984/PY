"""
ЗАДАНИЕ
Напишите программу на языке python, которая должна
Создать бд shopIT
Создать таблицу Компьютеры ( тип (ноутбук, стационарный компьютер, моноблок и т.д.), бренд, стоимость )

Сделать ЗАПРОСЫ и отобразить в консоле:
●	показать все компьютеры бренда “HP” 
(*усложненный вариант (НЕ ОБЯЗАТЕЛЬНО) HP может написано как HP, hp, Hp, Hp и 
в таких случаях все равно запрос должен отобразить все компьютеры бренда “HP”)
●	показать компьютеры стоимость которых более 40000
●	показать компьютеры типа “ноутбук” и стоимостью менее 30000
"""
from sqlite3 import *
import sqlite3 as sql

with sql.connect("shopIT.db") as con:
    cur = con.cursor()
    cur.executescript("""
                CREATE TABLE IF NOT EXISTS computers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                c_name VARCHAR(50) NOT NULL, 
                brand VARCHAR(50) NOT NULL,
                cost INTEGER NOT NULL);
                """)
    
    # cur.execute("""
    #             INSERT INTO `computers`(`c_name`, `brand`, `cost`) VALUES ('Ноутбук','HP',29000),
    #             ('Ноутбук','PHILIPS',30000),
    #             ('Ноутбук','MSI',70000),
    #             ('Стацианарный ПК','HP',95000),
    #             ('Моноблок','PHILIPS',80000);               
    #             """)
    
    result = cur.execute("""
                SELECT * FROM `computers`""")
    for row in result.fetchall():
        print(row)

    result = cur.execute("""
                SELECT * FROM computers WHERE `brand` = 'HP';
                """)
    print("""
     ●	показать все компьютеры бренда “HP” 
--------------------------------------------------""")
    for row in result.fetchall():
        print(row)

    result = cur.execute("""
                SELECT * FROM computers WHERE cost > 40000;
                """)
    print("""
     ●	показать компьютеры стоимость которых более 40000
-------------------------------------------------------------""")
    for row in result.fetchall():
        print(row)
    
    result = cur.execute("""
                SELECT * FROM `computers` WHERE `c_name` LIKE 'Ноутбук' AND `cost` < 30000
                """)
    print("""
     ●	показать компьютеры типа “ноутбук” и стоимостью менее 30000
----------------------------------------------------------------------""")
    for row in result.fetchall():
        print(row)