from tools import clear_screen, pause_screen


def view_employee(employee):
    if not employee:
        print("\nThere are no employees registered at the moment\n")
    else:
        print(
            f"\nThese are the employees entered in the registry: \n{employee}")


def add_employee(employee):
    clear_screen()
    name = str(input("Enter the employee's name: "))
    last_name = str(input("Enter the employee's last name: "))
    job_position = str(input("Enter the job: "))
    if len(name) and len(last_name) and len(job_position):
        employee_data = {
            'name': name,
            'last_name': last_name,
            'job_position': job_position
        }
        employee.append(employee_data)
        print("\n Employee successfully added ", employee_data)
    else:
        print("You must complete all employee information")
    pause_screen(2)


def update_employee(employee):
    print("actualizar empleado")


def delete_employee(employee):
    print("borrar empleado")


def end():
    print("\nthanks for using this program!")
