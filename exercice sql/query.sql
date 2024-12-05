/*Task 3*/

select
    s.name,
    c.course_name,
    c.credits
from
    enrollments e
join
    students s on e.student_id = s.student_id
join
    courses c on e.course_id = c.course_id;

select
    s.name
from
    students s
left join
    enrollments e on s.student_id = e.student_id
where
    e.enrollment_id is null;

/*Task 4*/

select
    c.course_name,
    count(e.enrollment_id) as nb_students
from
    courses c
left join
    enrollments e on c.course_id = e.course_id
group by
    c.course_id, c.course_name;


select
    c.course_name,
    count(e.enrollment_id) as enrolled_students,
    c.capacity
from
    courses c
join
    enrollments e on c.course_id = e.course_id
group by
    c.course_id, c.course_name, c.capacity
having
    count(e.enrollment_id) > c.capacity / 2;

/*Task 5*/

select
    s.name as student_name,
    count(e.enrollment_id) as enrolled_courses
from
    students s
join
    enrollments e on s.student_id = e.student_id
group by
    s.student_id, s.name
having
    count(e.enrollment_id) = (
        select
            max(course_count)
        from (
            select
                count(enrollment_id) as course_count
            from
                enrollments
            group by
                student_id
        ) as query
    );

select
    s.name as student_name,
    sum(c.credits) as total_credits
from
    students s
join
    enrollments e on s.student_id = e.student_id
join
    courses c on e.course_id = c.course_id
group by
    s.student_id, s.name;

select
    c.course_name
from
    courses c
left join
    enrollments e on c.course_id = e.course_id
group by
    c.course_id, c.course_name
having
    count(e.enrollment_id) = 0;



