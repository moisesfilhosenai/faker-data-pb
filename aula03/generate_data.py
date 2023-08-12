from random import randrange
from aula03.classes.category_course.category_course import CategoryCourse
from aula03.classes.category_course.category_course_db import create_categories_courses, to_csv_categories_courses
from aula03.classes.course.course import Course
from aula03.classes.course.course_db import create_courses, to_csv_courses, get_courses
from aula03.classes.student.student import Student
from aula03.classes.student.student_db import create_students, to_csv_students, get_students
from aula03.classes.discipline.discipline import Discipline
from aula03.classes.discipline.discipline_db import create_disciplines, to_csv_disciplines, get_disciplines_by_course_id
from aula03.classes.final_notes.final_notes import FinalNotes
from aula03.classes.final_notes.final_notes_db import create_final_notes, to_csv_final_notes
from aula03.classes.activity_note.activity_note import ActivityNote
from aula03.classes.activity_note.activity_note_db import create_activities_notes, to_csv_activities_notes


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
to_csv_disciplines("outputs/disciplinas.csv")

# Tabela medias
final_notes = []
courses = get_courses()
students =  get_students()

for student in students:
    course = courses[randrange(0, len(courses) - 1)]
    discipline = get_disciplines_by_course_id(course["id"])

    final_notes.append(FinalNotes(student_id=student["id"],
                                  course_id=course["id"],
                                  discipline_id=discipline["id"]))

create_final_notes(final_notes)
to_csv_final_notes("outputs/medias.csv")

# Tabela de notas atividades
activities_notes = []

for student in students:
    course = courses[randrange(0, len(courses) - 1)]
    discipline = get_disciplines_by_course_id(course["id"])

    activities_notes.append(ActivityNote(student_id=student["id"],
                                         discipline_id=discipline["id"]))

create_activities_notes(activities_notes)
to_csv_activities_notes("outputs/notas_atividades.csv")
