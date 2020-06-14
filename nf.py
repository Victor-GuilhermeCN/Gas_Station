from databank import Bank
from datetime import datetime
from Functions import *


class Nf:
    def __init__(self):
        self.bank = Bank()
        self.date = datetime.now().today().date()
        self.hour = datetime.now().time()

    def generates_nf_with_cpf(self, cpf, nf_value, nf_item, nf_amount):
        try:
            self.bank.cursor.execute('INSERT INTO nf (cpf, nf_value, nf_item, nf_amount, date_nf, nf_hour) VALUES (%s, '
                                     '%s, %s, %s, %s, %s)', (cpf, nf_value, nf_item, nf_amount, self.date, self.hour))
        except Exception as error_gen_nf:
            print('Generation error in NF')
            print(error_gen_nf)
        else:
            self.bank.con.commit()
            print('NF registered!')
            self.bank.con.close()

    def generates_nf_without_cpf(self, nf_value, nf_item, nf_amount):
        try:
            self.bank.cursor.execute('INSERT INTO nf (nf_value, nf_item, nf_amount, date_nf, nf_hour) VALUES (%s, %s, '
                                     '%s, %s, %s)', (nf_value, nf_item, nf_amount, self.date, self.hour))
        except Exception as error_g_without_cpf:
            print('Generetaion error in NF!')
            print(error_g_without_cpf)
        else:
            self.bank.con.commit()
            print('NF registered!')
            self.bank.con.close()

    def consulting_nf(self, id_nf):
        nf_cpf = []
        nf_value = []
        nf_item = []
        nf_amount = []
        date_nf = []
        nf_hour = []
        try:
            self.bank.cursor.execute('SELECT * FROM nf where id_nf =  %s', (id_nf))
            for i in self.bank.cursor.fetchall():
                nf_cpf.append(i[1])
                nf_value.append(i[2])
                nf_item.append(i[3])
                nf_amount.append(i[4])
                date_nf.append(i[5])
                nf_hour.append(i[6])
        except:
            print("There's no NF!")
        else:
            try:
                line()
                print(f'NF: Nº{id_nf} ', end='' )
                print(f'{date_nf[0]}|'.rjust(35), end=' ')
                print(f'{nf_hour[0]}')
                line()
                print(f'{nf_amount[0]}|'.ljust(0), end=' ')
                print(f'{nf_item[0]} '.center(0), end=' ')
                print(f'R$:{nf_value[0]}'.rjust(30))
                line()
                print(f'CPF: {nf_cpf[0]}')
            except:
                print("doesn't exist!")
                return False
            else:
                return True
