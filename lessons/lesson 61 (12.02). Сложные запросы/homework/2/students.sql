DROP TABLE Students;

CREATE TABLE Students (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_date DATE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    course_name TEXT NOT NULL,
    enrollment_date DATE NOT NULL
);
	
INSERT INTO Students (name, birth_date, email, course_name, enrollment_date) VALUES
    ('Иван Петров', '2000-05-15', 'ivan.petrov@email.com', 'Программирование', '2024-09-01'),
    ('Мария Смирнова', '2001-03-22', 'maria.smirnova@email.com', 'Дизайн', '2024-09-01'),
    ('Алексей Иванов', '2000-11-10', 'alexey.ivanov@email.com', 'Программирование', '2024-09-02'),
    ('Елена Козлова', '2002-07-08', 'elena.kozlova@email.com', 'Маркетинг', '2024-09-01'),
    ('Дмитрий Сидоров', '2001-12-03', 'dmitry.sidorov@email.com', 'Программирование', '2024-09-03'),
    ('Анна Новикова', '2000-09-18', 'anna.novikova@email.com', 'Английский язык', '2024-09-01'),
    ('Сергей Морозов', '2002-01-25', 'sergey.morozov@email.com', 'Программирование', '2024-09-02');	

	
SELECT name, email, enrollment_date
FROM Students
WHERE id IN (
    SELECT id
    FROM Students
    WHERE course_name = 'Программирование'
);