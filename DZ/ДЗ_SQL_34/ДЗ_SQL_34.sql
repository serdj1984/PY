-- 1. Есть бд «КОФЕЙНЯ»
-- необходимо спроектировать таблицы «КОФЕ», «БАРИСТА», «СМЕНА»
-- ЗАПРОСЫ:
-- Какой бариста на смену
-- Какой кофе продали на смене
-- Какой бариста продал кофе (пример «капучино 200 мл») на смене (пример 10.09. 2022)


/* -------------------- Создаем БД ----------------------- */
create database if not exists cafedb;                   -- */
use cafedb; -- переходим в базу                         -- */

/* ----------------- Создаем таблицы --------------------- */
create table if not exists barista(                     -- */
id integer primary key auto_increment,                  -- */
names varchar(50) not null                              -- */
);                                                      -- */
create table if not exists coffee(                      -- */
id integer primary key auto_increment,                  -- */
appellation varchar(50) not null                        -- */
);                                                      -- */
                                                        -- */
create table if not exists laborer(                     -- */
barista_id integer,                                     -- */
foreign key (barista_id) references barista(id),        -- */
coffee_id integer,                                      -- */
foreign key (coffee_id) references coffee(id),          -- */
`data_time` date not null                               -- */
);                                                      -- */

/* ------------------------------- Наполняем таблицы ----------------------------------- */
-- insert into barista (names) values ("Вася"), ("Петя");
-- insert into coffee (appellation) values  ("Эспрессо"), ("Капучино"), ("Латте"), ("Чай");
-- insert into laborer (barista_id, coffee_id, data_time) values ('1','1','2023-09-10'),
-- ('1','1','2023-09-10'),
-- ('1','2','2023-09-10'),
-- ('1','2','2023-09-10'),
-- ('2','2','2023-09-11'),
-- ('2','3','2023-09-11'),
-- ('2','4','2023-09-11');

/* ------------ Какой бариста на смене ----------------- */
-- SELECT laborer.data_time, barista.names FROM barista 
-- INNER JOIN laborer ON barista.id = laborer.barista_id

/* ------------ Какие кофе продали на смене ------------ */
-- SELECT laborer.data_time, coffee.appellation FROM coffee 
-- INNER JOIN laborer ON coffee.id = laborer.coffee_id;

-- SELECT * FROM cafedb.laborer
