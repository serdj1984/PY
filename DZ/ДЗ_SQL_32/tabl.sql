-- 4 задание
--   Создать таблицу врачей(имя, должность, ставка) 
--   добавить 3 любых врача показать всех врачай(имя должность ставка), 
--   должность которых равна Хирург



create database if not exists lessondb
use lessondb
create table if not exists doctors(
names varchar(50) not null,
post varchar(20) not null,
salary int(12)
);
insert doctors values ("Гебхардт Карл Франц", "Хирург", 500000),
("Эдриан Фернхэм", "Психолог", 300000),
("Николаева Лариса Ивановна","Терапевт", 100000),
("Коновалов Андрей Александрович", "Хирург", 400000);

SELECT * FROM lessondb.doctors;
SELECT * FROM lessondb.doctors WHERE post="Хирург";
