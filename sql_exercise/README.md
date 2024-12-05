# University Enrollment Management System

This repository contains a relational database design and SQL queries for managing students, courses, and enrollments at a university. The system tracks enrollments, course capacities, and student-specific statistics.

## Schema
The database consists of the following tables:

- **Students**: Contains student details like ID, name, age, and gender.
- **Courses**: Contains course details like ID, name, credits, and capacity.
- **Enrollments**: Links students to the courses they are enrolled in.

## Sample Data
- 5 students are registered.
- 4 courses are available, each with a specified capacity.
- 8 enrollments exist, including some courses reaching their capacity.

## Queries
This project includes the following SQL queries:

- List of all students and their enrolled courses.
- Students not enrolled in any courses.
- List of courses and the number of students enrolled.
- Courses where the number of enrollments exceeds half the course capacity.
- Students enrolled in the maximum number of courses.
- Total credits each student is taking.
- Courses with no enrollments.

## Files
- `schema.sql`: Contains the database schema with table creation statements and constraints.
- `data.sql`: Contains sample data insertion scripts.
- `queries.sql`: Contains SQL queries for retrieving and analyzing data.
