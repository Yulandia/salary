def show_employee(employee_name, salary=50000):
    output = employee_name + ' ' +"salary is" + ' ' + str(salary)
    print(output)

show_employee(employee_name='Yulia', salary=60000)
show_employee('Sveta', 70000)
show_employee('Nastya')