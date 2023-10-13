"""
ЗАДАНИЕ
создать таблицы для бд как на изображении

Можно воспользоваться запросом на вставку данных или придумать свои
INSERT INTO players (name, best_score) VALUES (“Миша”,200),
(“Ваня”,154),
(“Дима”,178),
(“Коля”,210);
INSERT INTO games (name, score, id_player) VALUES 
(“Миша”,110,1),
(“Миша”,200,1),
(“Дима”,178),
(“Коля”,10),
(“Коля”,30), 
(“Коля”,40),
(“Ваня”,154),
(“Коля”,210);
и написать запросы:
●	показать игроков и их кол-во игр
●	показать игроков и их итоговый счет за все сыгранные игры
●	Найти общее кол-во игр
●	Найти худший результат у каждого игрока

"""
from sqlite3 import *
import sqlite3 as sql

with sql.connect("sapper.db") as con:
    cur = con.cursor()

    cur.executescript("""
                CREATE TABLE IF NOT EXISTS players(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                best_score INTEGER NOT NULL);
                    """)
    
    cur.executescript("""
                CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                score INTEGER NOT NULL,
                id_player INTEGER,
                FOREIGN KEY (id_player) REFERENCES players(id));
                    """)
    
    # cur.execute("""
    #             INSERT INTO players (name, est_scoreb) VALUES 
    #             ('Миша',200),
    #             ('Ваня',154),
    #             ('Дима',178),
    #             ('Коля',210);
    #                 """)
    
    # cur.execute("""
    #             INSERT INTO games (name, score, id_player) VALUES 
    #             ('Миша',110,1),
    #             ('Миша',200,1),
    #             ('Дима',178,3),
    #             ('Коля',10,4),
    #             ('Коля',30,4),
    #             ('Коля',40,4),
    #             ('Ваня',154,2),
    #             ('Коля',210,4);
    #                 """)

    #  ●	показать игроков и их кол-во игр
    res = cur.execute("""
                      SELECT games.name, games.id FROM players 
                      INNER JOIN games ON players.id = games.id_player 
                      ORDER BY players.id DESC;
                      """)
    for row in res.fetchall():
        print(row)

    # ●	показать игроков и их итоговый счет за все сыгранные игры
    res = cur.execute("""
                      SELECT games.name, games.score FROM players 
                      INNER JOIN games ON players.id = games.id_player 
                      ORDER BY players.id DESC;
                      """)
    for row in res.fetchall():
        print(row)

    # ●	Найти общее кол-во игр
    res = cur.execute("""
                      SELECT games.id, games.name FROM players 
                      INNER JOIN games ON players.id = games.id_player 
                      ORDER BY games.id;
                      """)
    for row in res.fetchall():
        print(row)

    # ●	Найти худший результат у каждого игрока 
    res = cur.execute("""
                      SELECT name, score 
                      FROM games WHERE score = ( SELECT MIN(score) FROM games );
                      """)
    for row in res.fetchall():
        print(row)
