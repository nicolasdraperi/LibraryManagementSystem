For python : 

Features ✨

-View All Books: Displays all books in the library with their availability status.

-Search Books: Search for books by title or author.

-Add New Books: Add new books to the library.

-Borrow Books: Students can borrow books if they are available.

-Return Books: Students can return borrowed books.

-Persistent Data: Saves the library's state to a file (library_data.txt) for future use.

-Borrowing Limit: Each student can borrow up to 3 books at a time.

How to Run the Program 🚀

Prerequisites:

Python (version 3.6+).

Create the Data File:
Ensure a file named library_data.txt exists in the same directory as the script.
Format for the file:

Book Title,Author Name,True

Execute the script using the command:
python library_management_system.py

Interact with the Menu:
Use the menu to view, search, add, borrow, and return books.


For SQL : 


📁 File Structure
schema.sql: Contains the SQL commands to create the database schema, including students, courses, and enrollments tables.

data.sql: Populates the database with initial data for testing and practice.

query.sql: Includes all SQL queries for various tasks like fetching, analyzing, and cleaning data.

The database consists of three tables:

students

Tracks student details.

Columns:

student_id: Primary key (unique identifier).

name: Full name of the student.

age: Age of the student.

gender: Gender of the student.

courses

Stores information about university courses.

Columns:

course_id: Primary key (unique identifier).

course_name: Name of the course.

credits: Number of credits for the course.

capacity: Maximum number of students allowed.
enrollments


Links students to the courses they are enrolled in.

Columns:

enrollment_id: Primary key (auto-increment).

student_id: Foreign key referencing students.student_id.

course_id: Foreign key referencing courses.course_id.
