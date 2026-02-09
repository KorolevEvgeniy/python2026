DROP TABLE students;
CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER 
);
INSERT INTO students(id,name,age) VALUES ('1', '"Иван"', '20'),('2', '"Мария"', '22'),('3', '"Петр"', '19');

DROP TABLE sotrudniki;
CREATE TABLE sotrudniki(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
position TEXT NOT NULL,
salary REAL 
);
INSERT INTO sotrudniki(id,name,position,salary) VALUES ('1', '"Анна"', '"Разработчик"','50000'),('2', '"Олег"', '"Менеджер"','60000'),('3', '"Елена"', '"Дизайнер"','45000');
UPDATE sotrudniki SET salary = '65000' WHERE id = 2;

DROP TABLE prodagi;
CREATE TABLE prodagi(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
price REAL,
quantity REAL
);
INSERT INTO prodagi (id, name, price, quantity) VALUES ('1', '"Ноутбук"', '45000', '10'), ('2', '"Мышь"', '1500', '50'), ('3', '"Клавиатура"', '3000', '25'), ('4', '"Монитор"', '12000', '15');
DELETE FROM prodagi WHERE id = 3;