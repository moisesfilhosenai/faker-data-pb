"""
Geração de base de dados faker para curso de Power Bi (PB)
São 3 tabelas a serem geradas conforme arquivo aulas-power-bi.drawio aula02
Os dados são gerados com nomes despadronizados para corrigir dentro do PB
"""
from aula02.classes.employee.employee import Employee
from aula02.classes.employee.employee_db import create_employees, get_employees, to_csv_employees
from aula02.classes.benefit.benefit import Benefit
from aula02.classes.benefit.benefit_db import create_benefits, get_benefits, to_csv_benefits
from aula02.classes.position.position import Position
from aula02.classes.position.position_db import create_positions, get_positions, to_csv_positions


# Tabela Funcionários
employees = [Employee() for _ in range(5)]
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
    Position("Engenheiro Elétrico", 5.590),
    Position("Engenheiro Mecânico", 6.290),
    Position("Arquiteto", 7.890),
    Position("Analista de Sistemas", 5.190),
    Position("Desenvolvedor Júnior", 3.190),
    Position("Desenvolvedor Pleno", 5.290),
    Position("Desenvolvedor Sênior", 7.290),
    Position("Arquiteto de Software", 9.890),
    Position("Administrador Banco de Dados", 12.390),
    Position("Administrador Cloud", 13.190),
    Position("DevOps", 9.390),
    Position("Supervisor RH", 13.390),
    Position("Supervisor TI", 17.190),
    Position("Supervisor Produção", 14.790),
    Position("Motorista", 4.690),
    Position("Técnico", 3.190),
    Position("Diretor", 23.190)
]