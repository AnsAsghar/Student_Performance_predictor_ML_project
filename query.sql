CREATE DATABASE IF NOT EXISTS college;

USE college;

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(10),
    course VARCHAR(255),
    grade FLOAT
);

GRANT ALL PRIVILEGES ON college.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;

SELECT * FROM students;