CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL
);

CREATE TABLE Courses (
    CourseID INTEGER PRIMARY KEY,
    CourseName TEXT NOT NULL,
    Credits INTEGER NOT NULL
);

CREATE TABLE Enrollments (
    StudentID INTEGER,
    CourseID INTEGER,
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

INSERT INTO Students (StudentID, FirstName, LastName) VALUES 
    (1, 'Иван', 'Петров'),
    (2, 'Мария', 'Иванова'),
    (3, 'Алексей', 'Сидоров');

INSERT INTO Courses (CourseID, CourseName, Credits) VALUES 
    (101, 'Математический анализ', 4),
    (102, 'Физика', 3),
    (103, 'Программирование', 5);


INSERT INTO Enrollments (StudentID, CourseID) VALUES 
    (1, 101),  
    (1, 103), 
    (2, 102),  
    (2, 103),  
    (3, 101),  
    (3, 102);  

SELECT 
    s.LastName AS Фамилия,
    s.FirstName AS Имя,
    c.CourseName AS Название_курса
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Courses c ON e.CourseID = c.CourseID
ORDER BY s.LastName, s.FirstName, c.CourseName;

DELETE FROM Enrollments;
DELETE FROM Students;
DELETE FROM Courses;

SELECT 'Students' AS Table_Name, COUNT(*) AS Row_Count FROM Students
UNION ALL
SELECT 'Courses', COUNT(*) FROM Courses
UNION ALL
SELECT 'Enrollments', COUNT(*) FROM Enrollments;