from databank import Bank
from nf import Nf
from fidelity_system import Fidelity
from decimal import Decimal


class FuelPump:

    def __init__(self, id_comb, liter_value, qt_comb):
        self.id_comb = id_comb
        self.liter_value = liter_value
        self.qt_comb = qt_comb
        self.nf = Nf()
        self.fidelity = Fidelity()
        self.comb = Bank()

    def byvalue(self, id_comb, value):
        name_comb = self.comb.name_comb(id_comb)
        amount_liter = round(Decimal(value) / Decimal(self.comb.price_comb(id_comb)), 2)
        if amount_liter > self.comb.amount_comb(id_comb):
            print('Not fuel enough!')
        else:
            opt = input('Want the CPF in the note? [Y/N]: ').upper().strip()[0]
            if opt == 'Y':
                cpf = int(input('CPF: '))
                try:
                    self.comb.to_fuel(id_comb, (self.comb.amount_comb(id_comb) - amount_liter))
                    self.nf.generates_nf_with_cpf(str(cpf), value, name_comb, amount_liter)
                    self.fidelity.get_points(cpf)
                except Exception as error_value:
                    print('Problems in the system!')
                    print(error_value)
                else:
                    print(f'Refilled: ${value:.2f}\n'
                          f'Total liters: {amount_liter}')
            elif opt == 'N':
                try:
                    self.comb.to_fuel(id_comb, (self.comb.amount_comb(id_comb) - amount_liter))
                    self.nf.generates_nf_without_cpf(value, name_comb, amount_liter)
                except Exception as error_value:
                    print('Problems in the system!')
                    print(error_value)
                else:
                    print(f'Refilled: ${value:.2f}\n'
                          f'Total liters: {amount_liter}')

    def byliter(self, id_comb, qt_comb):
        name_comb = self.comb.name_comb(id_comb)
        amount_price = round(qt_comb * self.comb.price_comb(id_comb))
        if qt_comb > self.comb.amount_comb(id_comb):
            print("No fuel enough!")
        else:
            opt = input('Want the CPF in the note? [Y/N]').upper().strip()[0]
            if opt == 'Y':
                cpf = input('CPF: ')
                try:
                    self.comb.to_fuel(id_comb, (self.comb.amount_comb(id_comb) - qt_comb))
                    self.nf.generates_nf_with_cpf(str(cpf), amount_price, name_comb, qt_comb)
                    self.fidelity.get_points(cpf)
                except Exception as error_byliter_cpf:
                    print('Error in system')
                    print(error_byliter_cpf)
                else:
                    print(f'Refilled: ${amount_price:.2f}\n'
                          f'Total liters: {qt_comb}')
            elif opt == 'N':
                try:
                    self.comb.to_fuel(id_comb, (self.comb.amount_comb(id_comb) - qt_comb))
                    self.nf.generates_nf_without_cpf(amount_price, name_comb, qt_comb)
                except Exception as error_byliter_n_cpf:
                    print('Error in system!')
                    print(error_byliter_n_cpf)
                else:
                    print(f'Refilled: ${amount_price:.2f}\n'
                            f'Total liters: {qt_comb}')

