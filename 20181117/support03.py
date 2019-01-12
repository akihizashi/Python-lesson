print("大問3")

1
CREATE TABLE sample_person (
 id int not null auto_increment primary key,
 person_name varchar(20) not null,
 birth_place varchar(20) not null,
 height int not null,
 score int not null
);

2
INSERT INTO sample_person (person_name, birth_place, height, score)
VALUES
('山田太郎', '東京', 170, 80),
('鈴木次郎', '埼玉', 165, 70),
('佐藤三郎', '千葉', 162, 77),
('渡辺四郎', '神奈川', 180, 95);

3
SELECT AVG(score) FROM sample_person;
