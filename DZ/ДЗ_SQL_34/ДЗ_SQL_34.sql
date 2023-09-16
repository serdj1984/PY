create database if not exists cafedb;
use cafedb;

create table if not exists barista(
id integer primary key auto_increment,
names varchar(50) not null
);
create table if not exists coffee(
id integer primary key auto_increment,
appellation varchar(50) not null
);

create table if not exists laborer(
barista_id integer,
foreign key (barista_id) references barista(id),
coffee_id integer,
foreign key (coffee_id) references coffee(id),
`data_time` date not null
);
-- insert into barista (names) values ("Вася"), ("Петя");
-- insert into coffee (appellation) values  ("Эспрессо"), ("Капучино"), ("Латте"), ("Чай");
-- insert into laborer (barista_id, coffee_id, data_time) values ('1','1','2023-09-10'),
-- ('1','1','2023-09-10'),
-- ('1','2','2023-09-10'),
-- ('1','2','2023-09-10'),
-- ('2','2','2023-09-11'),
-- ('2','3','2023-09-11'),
-- ('2','4','2023-09-11');

-- SELECT laborer.data_time, barista.names FROM barista 
-- INNER JOIN laborer ON barista.id = laborer.barista_id

SELECT laborer.data_time, coffee.appellation FROM coffee 
INNER JOIN laborer ON coffee.id = laborer.coffee_id;

-- SELECT * FROM cafedb.laborer