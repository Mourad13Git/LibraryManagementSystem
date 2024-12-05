
INSERT INTO Students (student_id, name, age, gender) VALUES
(1, 'Alice Smith', 20, 'Female'),
(2, 'Bob Johnson', 22, 'Male'),
(3, 'Carol Davis', 21, 'Female'),
(4, 'David Brown', 23, 'Male'),
(5, 'Eva Wilson', 22, 'Female');


INSERT INTO Courses (course_id, course_name, credits, capacity) VALUES
(1, 'Database Systems', 3, 30),
(2, 'Operating Systems', 4, 40),
(3, 'Algorithms', 3, 25),
(4, 'Artificial Intelligence', 4, 30);


INSERT INTO Enrollments (student_id, course_id) VALUES
(1, 1), (1, 2), (2, 1), (2, 3), (3, 1),
(3, 4), (4, 2), (5, 3), (5, 4), (1, 3),
(2, 4), (4, 3);
