from decimal import *


def line():
    print('-' * 50)


def title(msg):
    line()
    print(msg.center(50))


def cpf_in_note():
    try:
        option = input('Want the CPF in the note? [Y/N]: ').upper().strip()[0]
        if option not in 'YN':
            print('Only Y/N')
            return cpf_in_note()
    except Exception:
        print('Only Y/N')
        return cpf_in_note()
    else:
        if option == 'Y':
            return True
        else:
            return False


def menu():
    title('MENU')
    line()
    print('[1] - Refueling the vehicle\n'
          '[2] - Register customer\n'
          '[3] - Consult promotion points\n'
          '[4] - Consult NF\n'
          '[5] - Exit')
    line()


def chosen_option_menu():
    try:
        option_menu = input('Which option: ')
        if option_menu not in '12345':
            print('Only numbers between 1-5')
            return chosen_option_menu()
    except Exception:
        print('Only numbers')
    else:
        return option_menu


def menu_fuel():
    title('FUEL PUMP')
    line()
    print('[1] - Fill by value\n'
          '[2] - Fill by liters\n'
          '[3] - Return Menu')


def liter_or_value():
    # Handling data entry option!
    try:
        line()
        liter_value = int(input('Which option: '))
        if liter_value > 3 or liter_value == 0:
            print('Only numbers between 1-3!')
            return liter_or_value()
    except:
        print('Only numbers!')
        return liter_or_value()
    else:
        line()
        return liter_value


def menu_comb_id():
    print('[1] - Gasoline \n'
          '[2] - Gas\n'
          '[3] - Diesel\n'
          '[4] - Alcohol\n'
          '[5] - Gasoline with additives\n'
          '[6] - Return')
    line()


def id_comb():
    try:
        id_fuel = input('Which fuel: ')
        line()
        if id_fuel not in '123456':
            print('Only numbers between 1-6')
            return id_comb()
    except:
        print('Only numbers!')
        return id_comb()
    else:
        if id_fuel == '6':
            return menu_fuel(), liter_or_value()
        else:
            return id_fuel


def getting_value():
    try:
        value = input('Value: RS:')
    except Exception:
        print('Only numbers!')
        return getting_value()
    else:
        return Decimal(value)


def getting_cpf():
    try:
        cpf = int(input('CPF: '))
        if len(str(cpf)) > 11 or len(str(cpf)) < 11:
            print('Only 11 numbers!')
    except Exception:
        print('Only numbers')
        return getting_cpf()
    else:
        return cpf


def getting_name():
    try:
        name = str(input('Name: '))
        if len(name) == 0:
            print('Empty field is not allowed!')
            return line(), getting_name()
    except Exception:
        print('Only letters!')
        return getting_name()
    else:
        return name


def getting_phone():
    try:
        phone = int(input('Phone: '))
        if len(str(phone)) < 9 or len(str(phone)) > 9:
            print('Only 9 numbers!')
            return getting_phone()
    except Exception:
        print('Only numbers!')
        return getting_phone()
    else:
        return phone


def getting_id_nf():
    try:
        id_nf = int(input('ID NF: '))
    except:
        print('Only numbers')
    else:
        return id_nf


# Function that returns to menu
def return_menu():
    try:
        rt_opt = input('Do you want to return to the main menu? [Y/N]: ').upper().strip()[0]
        if rt_opt not in 'YN':
            print('Only Y/N')
            return line(), return_menu()
    except:
        pass
    else:
        if rt_opt == 'Y':
            return menu()
        elif rt_opt == 'N':
            while True:
                print('See you soon!')
                break
