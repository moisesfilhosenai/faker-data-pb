"""
Geração de base de dados faker para curso de Power Bi (PB)
São 3 tabelas a serem geradas conforme arquivo aulas-power-bi.drawio aula02
Os dados são gerados com nomes despadronizados para corrigir dentro do PB
"""
from aula02.classes.employee.employee import Employee
from aula02.classes.employee.employee_db import create_employees, get_employees, to_csv_employees

employees = [Employee() for _ in range(5)]
create_employees(employees)
employees_db = get_employees()
to_csv_employees("outputs/funcionarios.csv")
"""
customers = [Customer() for _ in range(500)]
create_customers(customers)
customers_db = get_customers()
to_csv_customers("outputs/clientes.csv")
"""