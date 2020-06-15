from Functions import *
from fidelity_system import Fidelity
from nf import Nf
from client import Client
from fuel_pump import FuelPump


title('WELCOME TO THE KRUN GAS STATION')


def chosen_option():
    # Handling data entry in all cases
    menu()
    option_menu = chosen_option_menu()
    if option_menu == '1':
        menu_fuel()
        lv = liter_or_value()
        if lv == 1:
            menu_comb_id()
            FuelPump().byvalue(id_comb(), getting_value())
        elif lv == 2:
            menu_comb_id()
            FuelPump().byliter(id_comb(), getting_value())
        elif lv == 3:
            return chosen_option()
    elif option_menu == '2':
        title('REGISTRATION')
        line()
        Client().client_register(getting_cpf(), getting_name(), getting_phone())
    elif option_menu == '3':
        title('CONSULTING POINTS')
        line()
        Fidelity().consulting_points(str(getting_cpf()))
    elif option_menu == '4':
        title('NF CONSULTATIONS')
        line()
        Nf().consulting_nf(getting_id_nf())
    elif option_menu == '5':
        while True:
            print('See you soon!')
            break


chosen_option()
