from databank import Bank


class Client:

    def __init__(self):
        self.bank = Bank()

    def client_register(self, cpf, name, phone):
        try:
            self.bank.cursor.execute('INSERT INTO client (cpf, name, phone) VALUES (%s, %s, %s)', (cpf, name, phone))
        except Exception as error_insert_client:
            print('Insert Issues!')
            print(error_insert_client)
        else:
            self.bank.con.commit()
            print('Client registered!')
            self.bank.con.close()

    def select_client(self, cpf):
        client_name = []
        try:
            self.bank.cursor.execute('SELECT name from client where cpf = %s', cpf)
            for i in self.bank.cursor.fetchall():
                client_name.append(i[0])
        except Exception as error_select_name:
            print('Select issues!')
            print(error_select_name)
        else:
            print(f'Welcome {client_name[0]}!')

    def update_phone_client(self, cpf, phone):
        try:
            self.bank.cursor.execute('UPDATE client SET phone = %s where cpf = %s', (phone, cpf))
        except Exception as error_update_client:
            print('Update issues!')
            print(error_update_client)
        finally:
            self.bank.con.commit()
            print('Phone updated!')
            self.bank.con.close()

    def delete_client(self, cpf):
        try:
            self.bank.cursor.execute('DELETE from client where cpf = %s', (cpf,))
        except Exception as error_delete:
            print('Problems in the delete')
            print(error_delete)
        else:
            self.bank.con.commit()
            print('Client deleted successfully!')
            self.bank.con.close()

