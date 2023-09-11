from aula03.classes.student.student import Student
from aula03.classes.student.student_db import create_students, to_csv_students, get_students
from aula03.classes.discipline.discipline import Discipline
from aula03.classes.discipline.discipline_db import create_disciplines, to_csv_disciplines
from aula03.classes.activities.activity import Activity
from aula03.classes.activities.activity_db import create_activities, to_csv_activities, get_activities
from aula03.classes.notes.note import Note
from aula03.classes.notes.notes_db import create_notes, to_csv_notes

# Tabela alunos
students = [Student() for _ in range(50)]
create_students(students)
to_csv_students("outputs/alunos.csv")

# Tabela disciplinas
disciplines = [
    Discipline("Lógica de programação"),
    Discipline("HTML e CSS"),
    Discipline("Sistemas Operacionais"),
    Discipline("Programação Orientada a Objetos"),
    Discipline("Programação Web Backend"),
    Discipline("Programação Web Frontend"),
    Discipline("Desenvolvimento de aplicativos Android")
]
create_disciplines(disciplines)
to_csv_disciplines("outputs/disciplines.csv")

# Tabela atividades
activities = [
    Activity("Resolver algoritimo viagem", 1),
    Activity("Resolver algoritimo salario", 1),
    Activity("Resolver algoritimo tempo", 1),
    Activity("Resolver algoritimo números primos", 1),
    Activity("Design responsivo", 2),
    Activity("Desenvolvendo site para loja", 2),
    Activity("Desenvolvendo site blog", 2),
    Activity("Criando bons estilos css", 2),
    Activity("Arquitetura SO", 2),
    Activity("Usuários e grupos", 2),
    Activity("Instalando SO", 2),
    Activity("Criando classes", 3),
    Activity("Herança", 3),
    Activity("Interfaces", 3),
    Activity("Arquitetura de API Rest", 4),
    Activity("Arquitetura Moderna de Backend", 4),
    Activity("API para loja", 4),
    Activity("Criando componentes com Angular", 5),
    Activity("Frontend moderno", 5),
    Activity("Componentizando site", 5),
    Activity("APP abastece", 6),
    Activity("APP todolist", 6),
    Activity("APP agenda", 6)
]
create_activities(activities)
to_csv_activities("outputs/atividades.csv")

# Tabela notas
notes = []
for student in get_students():
    for activity in get_activities():
        notes.append(Note(student_id=student["id"], activity=activity))

create_notes(notes)
to_csv_notes("outputs/notas.csv")
