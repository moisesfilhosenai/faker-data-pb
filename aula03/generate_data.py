from aula03.classes.category_course.category_course import CategoryCourse
from aula03.classes.category_course.category_course_db import create_categories_courses

categories_courses = [
    CategoryCourse("Curso Técnico"),
    CategoryCourse("Graduação"),
    CategoryCourse("Pós graduação")
]
create_categories_courses(categories_courses)
