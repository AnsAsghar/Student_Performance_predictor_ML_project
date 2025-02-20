-- Create and use the database
CREATE DATABASE IF NOT EXISTS college;
USE college;

-- Create the student table with relevant columns for ML analysis
CREATE TABLE IF NOT EXISTS student (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    course VARCHAR(50),
    total_marks FLOAT,
    attendance_percentage FLOAT,
    extra_curricular_activities INT,
    internship_experience BOOLEAN,
    placement_status BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some sample data
INSERT INTO student (name, age, gender, course, total_marks, attendance_percentage, extra_curricular_activities, internship_experience, placement_status)
VALUES
    ('John Doe', 21, 'Male', 'Computer Science', 85.5, 92.0, 2, true, true),
    ('Jane Smith', 20, 'Female', 'Data Science', 88.7, 95.0, 3, true, true),
    ('Mike Johnson', 22, 'Male', 'AI/ML', 78.9, 88.0, 1, false, false),
    ('Sarah Williams', 21, 'Female', 'Computer Science', 92.3, 98.0, 4, true, true),
    ('Tom Brown', 23, 'Male', 'Data Science', 76.5, 85.0, 2, true, false);

-- Select all records from student table
SELECT * FROM student;