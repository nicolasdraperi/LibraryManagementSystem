
insert into students (student_id, name, age, gender) values
(1, 'Alice Smith', 20, 'female'),
(2, 'Bob Johnson', 22, 'male'),
(3, 'Charlie Brown', 19, 'male'),
(4, 'Diana Prince', 21, 'female'),
(5, 'Ethan Hunt', 23, 'male');


insert into courses (course_id, course_name, credits, capacity) values
(101, 'Introduction to Programming', 3, 3),
(102, 'Database Systems', 4, 2),
(103, 'Operating Systems', 3, 5),
(104, 'Artificial Intelligence', 4, 4);


insert into enrollments (enrollment_id, student_id, course_id) values
(1, 1, 101),
(2, 2, 101),
(3, 3, 101),
(4, 4, 102),
(5, 5, 102),
(6, 1, 103),
(7, 2, 103),
(8, 3, 104);



insert into students (student_id, name, age, gender) values
(6, 'Fiona Taylor', 24, 'female'); /*Juste pour la task 3*/

insert into courses (course_id, course_name, credits, capacity) values
(105, 'Quantum Computing', 4, 10); /*Juste pour la task 5*/

/*
Pour préciser les premiere ligne type instert into sont fait a la main, la gen de donnée est faite par chatgtp
(j'avais pas d'idée et peu de temps ;-;)
*/


