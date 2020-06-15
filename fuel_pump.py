from databank import Bank
from Functions import *
from nf import Nf
from fidelity_system import Fidelity
from decimal import Decimal


class FuelPump:

    def __init__(self):
        self.nf = Nf()
        self.fidelity = Fidelity()
        self.comb = Bank()

    def byvalue(self, id_fuel, value):
        name_comb = self.comb.name_comb(id_fuel)
        amount_liter = round(Decimal(value) / Decimal(self.comb.price_comb(id_fuel)), 2)
        if amount_liter > self.comb.amount_comb(id_fuel):
            print('Not fuel enough!')
        else:
            cpf_note = cpf_in_note()
            if cpf_note:
                cpf = getting_cpf()
                try:
                    self.comb.to_fuel(id_fuel, (self.comb.amount_comb(id_fuel) - amount_liter))
                    self.nf.generates_nf_with_cpf(str(cpf), value, name_comb, amount_liter)
                    self.fidelity.get_points(cpf)
                except Exception as error_value:
                    print('Problems in the system!')
                    print(error_value)
                else:
                    print(f'Refilled: ${value:.2f}\n'
                          f'Total liters: {amount_liter}')
            else:
                try:
                    self.comb.to_fuel(id_fuel, (self.comb.amount_comb(id_fuel) - amount_liter))
                    self.nf.generates_nf_without_cpf(value, name_comb, amount_liter)
                except Exception as error_value:
                    print('Problems in the system!')
                    print(error_value)
                else:
                    print(f'Refilled: ${value:.2f}\n'
                          f'Total liters: {amount_liter}')

    def byliter(self, id_comb, qt_comb):
        name_comb = self.comb.name_comb(id_comb)
        amount_price = round(Decimal(qt_comb) * Decimal(self.comb.price_comb(id_comb)))
        if qt_comb > self.comb.amount_comb(id_comb):
            print("No fuel enough!")
        else:
            cpf_note = cpf_in_note()
            if cpf_note:
                cpf = getting_cpf()
                try:
                    self.comb.to_fuel(id_comb, (Decimal(self.comb.amount_comb(id_comb)) - Decimal(qt_comb)))
                    self.nf.generates_nf_with_cpf(str(cpf), amount_price, name_comb, Decimal(qt_comb))
                    self.fidelity.get_points(cpf)
                except Exception as error_byliter_cpf:
                    print('Error in system')
                    print(error_byliter_cpf)
                else:
                    print(f'Refilled: ${amount_price:.2f}\n'
                          f'Total liters: {qt_comb}')
            else:
                try:
                    self.comb.to_fuel(id_comb, (self.comb.amount_comb(id_comb) - qt_comb))
                    self.nf.generates_nf_without_cpf(amount_price, name_comb, qt_comb)
                except Exception as error_byliter_n_cpf:
                    print('Error in system!')
                    print(error_byliter_n_cpf)
                else:
                    print(f'Refilled: ${amount_price:.2f}\n'
                          f'Total liters: {qt_comb}')
