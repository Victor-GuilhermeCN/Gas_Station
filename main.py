from Functions import *
from fidelity_system import Fidelity
from nf import Nf
from client import Client
from fuel_pump import FuelPump
from decimal import Decimal


title('WELCOME TO THE KRUN GAS STATION')


def menu():
    title('MENU')
    line()
    print('[1] - Refueling the vehicle\n'
          '[2] - Register customer\n'
          '[3] - Consult promotion points\n'
          '[4] - Consult NF\n'
          '[5] - Exit')
    line()
    chosen_option()


def chosen_option():
    # Handling data entry Option
    try:
        opt = input('Which option: ')
        if opt not in '12345':
            print('Only numbers between 1-5!')
            return line(), chosen_option()
    except Exception as error_chosen_option:
        print('Error')
        print(error_chosen_option)
    else:
        if opt == '1':
            def menu_fuel():
                title('FUEL PUMP')
                line()
                print('[1] - Fill by liters\n'
                      '[2] - Fill by value\n'
                      '[3] - Return Menu')

            def liter_or_value():
                # Handling data entry option!
                try:
                    line()
                    liter_value = int(input('Wich option: '))
                    if liter_value > 3:
                        print('Only numbers between 1-3!')
                        return liter_or_value()
                except:
                    print('Only numbers!')
                    return liter_or_value()
                else:
                    if liter_value == 1:
                        #  Handling data entry ID Fuel
                        def id_comb():
                            print('[1] - Gasoline \n'
                                  '[2] - Gas\n'
                                  '[3] - Diesel\n'
                                  '[4] - Alcohol\n'
                                  '[5] - Gasoline with additives\n'
                                  '[6] - Return')
                            line()
                            try:
                                id_combs = input('Which fuel: ')
                                line()
                                if id_combs not in '123456':
                                    print('Only numbers between 1-6')
                                    return id_comb()
                            except:
                                print('Only numbers!')
                                return id_comb()
                            else:
                                if id_combs == '6':
                                    return menu_fuel(), liter_or_value()

                                # Handling data entry liters
                                def value_liters():
                                    try:
                                        liters = float(input('Liters: '))
                                    except:
                                        print('Only numbers!')
                                        return value_liters()
                                    else:
                                        # Running the supply
                                        FuelPump().byliter(id_combs, Decimal(liters))
                                value_liters()
                        id_comb()
                    if liter_value == 2:
                        def id_comb():
                            print('[1] - Gasoline \n'
                                  '[2] - Gas\n'
                                  '[3] - Diesel\n'
                                  '[4] - Alcohol\n'
                                  '[5] - Gasoline with additives\n'
                                  '[6] - Return')
                            line()
                            try:
                                id_combs = input('Which fuel: ')
                                line()
                                if id_combs not in '123456':
                                    print('Only numbers between 1-6')
                                    return id_comb()
                            except:
                                print('Only numbers!')
                                return id_comb()
                            else:
                                if id_combs == '6':
                                    # Returnin to menu
                                    return menu_fuel(), liter_or_value()

                                def value_fill():
                                    # Handling data entry Value
                                    try:
                                        value = float(input('Value: '))
                                    except:
                                        print('Only numbers!')
                                        return value_fill()
                                    else:
                                        # Running the supply
                                        FuelPump().byvalue(id_combs, value)
                                value_fill()
                        id_comb()

            menu_fuel()
            liter_or_value()

        elif opt == '2':
            title('REGISTRATION')
            line()

            def getting_data():
                # Handling data entry CPF
                def getting_cpf():
                    try:
                        cpf = int(input('CPF: '))
                        if len(str(cpf)) > 11 or len(str(cpf)) < 11:
                            print('Only 11 numbers!')
                            return getting_data()
                    except:
                        print('Only numbers!')
                        return getting_cpf()
                    else:
                        name = input('Name: ')

                        # Handling data entry phone
                        def getting_phone():
                            try:
                                phone = int(input('Phone: '))
                                if len(str(phone)) > 9 or len(str(phone)) < 9:
                                    print('Only 9 numbers!')
                                    return getting_phone()
                            except:
                                print('Only numbers!')
                                return getting_phone()
                            else:
                                # Checking if the user is already registered
                                client_insert = Client().client_register(cpf, name, phone)
                                if client_insert == True:
                                    pass
                                elif client_insert == False:
                                    print("You're already registered!")
                                line()
                                return_menu()

                        getting_phone()
                getting_cpf()
            getting_data()

        elif opt == '3':
            title('CONSULTING POINTS')
            line()

            def verifying_cpf():
                try:
                    cpf = int(input('Please insert your CPF: '))
                    if len(str(cpf)) > 11 or len(str(cpf)) < 11:
                        print('Only 11 numbers!')
                        return verifying_cpf()
                except:
                    print('Only numbers!')
                    return verifying_cpf()
                else:
                    return line(), Fidelity().consulting_points(cpf), line(), return_menu()
            verifying_cpf()
        elif opt == '4':
            title('NF CONSULTATIONS')
            line()

            def get_id_nf():
                # Handling data entry ID_NF
                try:
                    id_nf = int(input('ID NF: '))
                except:
                    print('Only numbers')
                else:
                    # Running the consultation in the databank
                    result_consult = Nf().consulting_nf(id_nf)
                    # Verifying if the consultation it's right
                    if result_consult == True:
                        return line(), return_menu()
                    elif result_consult == False:
                        return line(), get_id_nf()
            get_id_nf()
        elif opt == '5':
            # Exiting the application
            while True:
                print('See you soon!')
                break


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


menu()