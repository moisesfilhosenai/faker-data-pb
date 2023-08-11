from random import randrange
from aula03.classes.category_course.category_course import CategoryCourse
from aula03.classes.category_course.category_course_db import create_categories_courses, to_csv_categories_courses
from aula03.classes.course.course import Course
from aula03.classes.course.course_db import create_courses, to_csv_courses
from aula03.classes.student.student import Student
from aula03.classes.student.student_db import create_students, to_csv_students
from aula03.classes.discipline.discipline import Discipline
from aula03.classes.discipline.discipline_db import create_disciplines, to_csv_disciplines

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
    Course("Ciências Contábeis", 3),
]
create_courses(courses)
to_csv_courses("outputs/cursos.csv")

# Tabela alunos
students = [Student() for _ in range(50)]
create_students(students)
to_csv_students("outputs/alunos.csv")

# Tabela disciplinas
disciplines = [
    Discipline("Administração", 1),
    Discipline("Ergonomia", 1),
    Discipline("Técnicas de enfermagem", 1),
    Discipline("Comandos elétricos", 2),
    Discipline("CLP", 2),
    Discipline("Eletrônica Digital", 2),
    Discipline("Lógica de programação", 3),
    Discipline("Orientação a Objetos", 3),
    Discipline("Programação com Java", 3),
    Discipline("Programação com Python", 3),
    Discipline("Engenharia de software", 4),
    Discipline("Banco de dados", 4),
    Discipline("Projetos de software", 4),
    Discipline("Testes de sistemas", 4),
    Discipline("Negócios empresariais", 5),
    Discipline("Excel avançado", 5),
    Discipline("Startup de sucesso", 5),
    Discipline("Cálculos com R", 6),
    Discipline("Análise de elementos da lavoura", 6),
    Discipline("Cálculo para negócios", 7),
    Discipline("Geração de relatórios empresariais", 7)
]
create_disciplines(disciplines)
to_csv_disciplines("outputs/disciplinas")
