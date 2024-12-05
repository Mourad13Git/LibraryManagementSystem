--query 1
SELECT s.name AS student_name, c.course_name, c.credits
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;

--query 2
SELECT s.name AS student_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;

--query 3
SELECT c.course_name, COUNT(e.student_id) AS students_enrolled
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

--query 4
SELECT c.course_name, COUNT(e.student_id) AS students_enrolled
FROM Courses c
JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
HAVING COUNT(e.student_id) > (c.capacity / 2);

--query 5
SELECT s.name AS student_name, COUNT(e.course_id) AS courses_enrolled
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id
ORDER BY courses_enrolled DESC
LIMIT 1;

--query 6
SELECT s.name AS student_name, SUM(c.credits) AS total_credits
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
GROUP BY s.student_id;

--query 7
SELECT c.course_name
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
WHERE e.enrollment_id IS NULL;

--task 6 : implement constraints
-- check enrolling students in a course if it has reached its capacity
ALTER TABLE Enrollments
ADD CONSTRAINT check_capacity
CHECK (course_id IN (
    SELECT course_id FROM Courses
    WHERE (SELECT COUNT(*) FROM Enrollments WHERE course_id = Courses.course_id) < Courses.capacity
));

-- student max enrolling courses = 5
CREATE TRIGGER max_courses_per_student
BEFORE INSERT ON Enrollments
FOR EACH ROW
BEGIN
    DECLARE num_courses INT;
    SELECT COUNT(*) INTO num_courses
    FROM Enrollments
    WHERE student_id = NEW.student_id;
    
    IF num_courses >= 5 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'A student cannot enroll in more than 5 courses';
    END IF;
END;

--task 7
-- remove all enrollments
DELETE FROM Enrollments
WHERE course_id = 1;  

--delete students with 00 enrollments
DELETE FROM Students
WHERE student_id NOT IN (SELECT DISTINCT student_id FROM Enrollments);
--

