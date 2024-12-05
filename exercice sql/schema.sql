/*
create database exercicesql;
use exercicesql;
*/
create table students (
    student_id int primary key,
    name varchar(50),
    age int,
    gender varchar(10)
);

create table courses (
    course_id int primary key,
    course_name varchar(50),
    credits int,
    capacity int
);

create table enrollments (
    enrollment_id int primary key auto_increment,
    student_id int,
    course_id int,
    foreign key (student_id) references students(student_id),
    foreign key (course_id) references courses(course_id)
);


/* Tache 7*/

delete from enrollments
where course_id = 101;

delete from students
where student_id not in (
    select distinct student_id
    from enrollments
);


