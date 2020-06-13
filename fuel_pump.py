from databank import Bank


class FuelPump:

    def __init__(self, id_comb, liter_value, qt_comb):
        self.id_comb = id_comb
        self.liter_value = liter_value
        self.qt_comb = qt_comb

    def byvalue(self, id_comb, value):
        comb = Bank()
        price_liter = round(value / comb.price_comb(id_comb), 2)
        if price_liter > comb.amount_comb(id_comb):
            print('Not fuel enough!')
        else:
            comb.to_fuel(id_comb, (comb.amount_comb(id_comb) - price_liter))
            print(f'Refilled: ${value:.2f}\n'
                  f'Total liters: {price_liter}')

    def byliter(self, id_comb, qt_comb):
        comb = Bank()
        price_liter = round(qt_comb * comb.price_comb(id_comb))
        if qt_comb > comb.amount_comb(id_comb):
            print("No fuel enough!")
        else:
            comb.to_fuel(id_comb, (comb.amount_comb(id_comb) - qt_comb))
            print(f'Refilled: ${price_liter:.2f}\n'
                  f'Total liters: {qt_comb}')


c = FuelPump(1, 30, 40)
c.byvalue(1, 30)
