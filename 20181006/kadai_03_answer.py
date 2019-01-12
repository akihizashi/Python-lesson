問 1-1
CREATE database person_db DEFAULT CHARACTER SET utf8;

問 1-2
grant all privileges on person_db.*to person_user@'localhost' identified by 'person_pass' with grant option;

grant all privileges on eri_db.*to eri_user@'localhost' identified by 'eri_pass' with grant option;

CREATE USER 'eri_user'@'localhost' IDENTIFIED BY 'eri_pass';
GRANT ALL PRIVILEGES ON *eri_db.* TO 'eri_user'@'localhost' WITH GRANT OPTION;

問 1-3
use person_db;
CREATE TABLE person_tb(
id int(11) not null auto_increment primary key, name varchar(20) not null,
age int(11) not null,
language varchar(20) not null
);

問 1-4
desc person_tb;

問 1-5
INSERT INTO person_tb(
name , age , language
) VALUES ('yamadata',19,'PHP'),
('suzuki',22,'Java'),
('tanaka',18,'Ruby'),
('watanabe',25,'C'),
('satou',33,'Perl');

問 1-6
SELECT * from person_tb;

問 1-7
SELECT * from person_tb where age > '20';

問 1-8
UPDATE person_tb SET age = 23, language = 'Python' WHERE id = 2;

問 1-9
SELECT sum(age) as '合計' , avg(age) as '平均' FROM person_tb;
