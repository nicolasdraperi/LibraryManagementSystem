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
