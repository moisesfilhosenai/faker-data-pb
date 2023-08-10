from random import randrange
from aula03.classes.category_course.category_course import CategoryCourse
from aula03.classes.category_course.category_course_db import create_categories_courses, to_csv_categories_courses
from aula03.classes.course.course import Course
from aula03.classes.course.course_db import create_courses, to_csv_courses
from aula03.classes.student.student import Student
from aula03.classes.student.student_db import create_students, to_csv_students

# Tabela categoria cursos
categories_courses = [
    CategoryCourse("Curso Técnico"),
    CategoryCourse("Graduação"),
    CategoryCourse("Pós graduação")
]
create_categories_courses(categories_courses)
to_csv_categories_courses("outputs/categorias_cursos.csv")

# Tabela cursos
courses = [
    Course("Técnico em enfermagem", 1),
    Course("Técnico em eletroeletrônica", 1),
    Course("Técnico em informática", 1),
    Course("Análise e Desenvolvimento de Sistemas", 2),
    Course("Administração", 2),
    Course("Agronegócio", 2),
    Course("Biologia", 2),
    Course("Medicina", 2),
    Course("Arquitetura e Design", 3),
    Course("Ciências Contábeis", 3),
    Course("MBA Agronegócio", 3),
    Course("Gestão Financeira", 3),
]
create_courses(courses)
to_csv_courses("outputs/cursos.csv")

# Tabela alunos
students = [Student() for _ in range(50)]
create_students(students)
to_csv_students("outputs/alunos.csv")