"""
Geração de base de dados faker para curso de Power Bi (PB)
São 3 tabelas a serem geradas conforme arquivo aulas-power-bi.drawio aula02
Os dados são gerados com nomes despadronizados para corrigir dentro do PB
"""
from random import randrange
from aula02.classes.employee.employee import Employee
from aula02.classes.employee.employee_db import create_employees, get_employees, to_csv_employees
from aula02.classes.benefit.benefit import Benefit
from aula02.classes.benefit.benefit_db import create_benefits, get_benefits, to_csv_benefits
from aula02.classes.position.position import Position
from aula02.classes.position.position_db import create_positions, get_positions, to_csv_positions
from aula02.classes.humnan_resources.human_resource import HumnanResource
from aula02.classes.humnan_resources.humnan_resource_db import create_humnan_resources, to_csv_humnan_resouces

# Tabela Funcionários
employees = [Employee() for _ in range(50)]
create_employees(employees)
employees_db = get_employees()
to_csv_employees("outputs/funcionarios.csv")

# Tabela Benefícios
vr = 240.99
vt = 99.99
odonto = 69.99
saude = 329.99

benefits = [
    Benefit("VR", vr),
    Benefit("VT", vt),
    Benefit("Odonto", odonto),
    Benefit("Saúde", saude),
    Benefit("VR+VT", vr+vt),
    Benefit("VR+Odonto", vr+odonto),
    Benefit("VR+Saúde", vr+saude),
    Benefit("VT+Odonto", vr+odonto),
    Benefit("VT+Saúde", vt+saude),
    Benefit("Odonto+Saúde", odonto+saude)
]

create_benefits(benefits)
benefits_db = get_benefits()
to_csv_benefits("outputs/beneficios.csv")

# Tabela Cargos
positions = [
    Position("Engenheiro Elétrico", 5590),
    Position("Engenheiro Mecânico", 6290),
    Position("Arquiteto", 7890),
    Position("Analista de Sistemas", 5190),
    Position("Desenvolvedor Júnior", 3190),
    Position("Desenvolvedor Pleno", 5290),
    Position("Desenvolvedor Sênior", 7290),
    Position("Arquiteto de Software", 9890),
    Position("Administrador Banco de Dados", 12390),
    Position("Administrador Cloud", 13190),
    Position("DevOps", 9390),
    Position("Supervisor RH", 13390),
    Position("Supervisor TI", 17190),
    Position("Supervisor Produção", 14790),
    Position("Motorista", 4690),
    Position("Técnico", 3190),
    Position("Diretor", 23190)
]

create_positions(positions)
positions_db = get_positions()
to_csv_positions("outputs/cargos.csv")

# Tabela Recursos Humanos
humnan_resources = []
employees_benefits = []

for employee in employees_db:
    benefit = benefits_db[randrange(0, len(benefits_db) - 1)]
    position = positions_db[randrange(0, len(positions_db) - 1)]
    employees_benefits.append({
        "employee": employee, "benefit": benefit, "position": position
    })

for year in range(2010, 2024):
    for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        for employees_benefit in employees_benefits:
            employee = employees_benefit.get("employee")
            benefit = employees_benefit.get("benefit")
            position = employees_benefit.get("position")

            humnan_resources.append(HumnanResource(employee_id=employee["id"],
                                                   benefit_id=benefit["id"],
                                                   position_id=position["id"],
                                                   month=month,
                                                   year=year))

create_humnan_resources(humnan_resources)
to_csv_humnan_resouces("outputs/recursos_humanos.csv")
