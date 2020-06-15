from databank import Bank
from client import Client


class Fidelity:

    def __init__(self):
        self.bank = Bank()
        self.client = Client()

    # Adding loyalty points
    def get_points(self, cpf):
        value_nf = []
        try:
            self.bank.cursor.execute('SELECT SUM(nf_value) FROM nf where cpf = %s', (cpf,))
            for i in self.bank.cursor.fetchall():
                value_nf.append(i[0])
        except Exception as error_fidelity:
            print('Error in the system!')
            print(error_fidelity)
        else:
            points = round((value_nf[0] / 10), 2)
            self.bank.cursor.execute('UPDATE client set points_fidelity = %s where cpf = %s', (points, cpf))
            self.bank.con.commit()
            self.bank.con.close()

    # Querying total customer loyalty points
    def consulting_points(self, cpf):
        amount_points = []
        client_name = self.client.select_client_name(cpf)
        if len(client_name) == 0:
            print("You're not registered!")
        else:
            try:
                self.bank.cursor.execute('SELECT points_fidelity from client where cpf = %s', (cpf,))
                for i in self.bank.cursor.fetchall():
                    amount_points.append(i[0])
            except Exception:
                print("You still don't have points!")
            else:
                if len(amount_points) == 1:
                    amount_points = '0'
                print(f'Hi {client_name[0]},')
                print(f'Your points in our loyalty program are: {amount_points[0]}')
