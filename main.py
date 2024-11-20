from display_menu import display_menu as menu
from tools import clear_screen
from crud import view_employee, add_employee, update_employee, delete_employee, end


def main():
    employee = []
    while True:
        clear_screen()
        menu()
        option = int(input("Enter the desired option, input only numbers: "))
        if option == 1:
            view_employee(employee)
        elif option == 2:
            add_employee(employee)
        elif option == 3:
            update_employee(employee)
        elif option == 4:
            delete_employee(employee)
        elif option == 0:
            end()
            break
        else:
            print("select a valid option!")


if __name__ == "__main__":
    main()
