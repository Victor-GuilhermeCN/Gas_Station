from databank import Bank
from datetime import datetime


class Nf:

    def __init__(self):
        self.bank = Bank()
        self.date = datetime.now().today().date()
        self.hour = datetime.now().time()

    def generates_nf_with_cpf(self, cpf, nf_value, nf_item):
        try:
            self.bank.cursor.execute('INSERT INTO nf (cpf, nf_value, nf_item, date_nf, nf_hour) VALUES (%s, %s, %s, %s,'
                                     '%s)', (cpf, nf_value, nf_item, self.date, self.hour))
        except Exception as error_gen_nf:
            print('Generation error in NF')
            print(error_gen_nf)
        else:
            self.bank.con.commit()
            print('NF registered!')
            self.bank.con.close()

    def generates_nf_without_cpf(self, nf_value, nf_item):
        try:
            self.bank.cursor.execute('INSERT INTO nf (nf_value, nf_item, date_nf, nf_hour) VALUES (%s, %s, %s,%s)',
                                     (nf_value, nf_item, self.date, self.hour))
        except Exception as error_g_without_cpf:
            print('Generetaion error in NF!')
            print(error_g_without_cpf)
        else:
            self.bank.con.commit()
            print('NF registered!')
            self.bank.con.close()
