import pymysql

# Starting Database and connecting


class Bank:

    def __init__(self):
        self.con = pymysql.connect(db='fuelpump', user='root', passwd='')
        self.cursor = self.con.cursor()

    def create_table_tank(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS( id_comb int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT, name_comb'
                            'varchar(255) not null, qt_comb decimal(10,2) not null, price decimal(10,2) not null)')

    def create_table_client(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS(cpf varchar(11) PRIMARY KEY NOT NULL, name varchar(255)'
                            ' not null, phone varchar(9) not null)')

    def insert_comb(self, name_comb, qt_comb, price):
        try:
            self.cursor.execute('INSERT INTO tank (name_comb, qt_comb, price) VALUES (%s, %s, %s)',
                                (name_comb, round(qt_comb, 2), round(price, 2)))
        except Exception as error_insert:
            print('Problems in insert')
            print(error_insert)
        else:
            self.con.commit()
            self.con.close()

    def update_price(self, id_comb, new_price):
        try:
            self.cursor.execute('UPDATE tank SET price = %s WHERE id_comb = %s', (new_price, id_comb))
        except Exception as error_up_price:
            print('Price update error!')
            print(error_up_price)
        else:
            self.con.commit()
            print('Price updated!')
            self.con.close()

    def amount_comb(self, id_comb):
        qt_comb = []
        # Consulting the amount of fuel.
        try:
            self.cursor.execute('SELECT qt_comb from tank where id_comb = %s', id_comb)
            for i in self.cursor.fetchall():
                qt_comb.append(i[0])
        except Exception as error_select_qt:
            print('Problems 1')
            print(error_select_qt)
        else:
            self.con.commit()
            return qt_comb[0]

    def price_comb(self, id_comb):
        price_comb = []
        # Consulting the price of fuel.
        try:
            self.cursor.execute('SELECT price from tank where id_comb = %s', id_comb)
            for i in self.cursor.fetchall():
                price_comb.append(i[0])
        except Exception as error_select_qt:
            print('Problems 1')
            print(error_select_qt)
        else:
            self.con.commit()
            return price_comb[0]

    def name_comb(self, id_comb):
        name_comb = []
        # Consulting the name of the fuel by ID.
        try:
            self.cursor.execute('SELECT name_comb from tank where id_comb = %s', (id_comb,))
            for i in self.cursor.fetchall():
                name_comb.append(i[0])
        except Exception as error_select_name_comb:
            print('Error in select name!')
            print(error_select_name_comb)
        else:
            return name_comb[0]

    def to_fuel(self, id_comb, to_fuel):
        self.amount_comb(id_comb)
        try:
            self.cursor.execute('UPDATE tank set qt_comb = %s WHERE id_comb = %s', (round(to_fuel, 2), id_comb))
        except Exception as error_to_fuel:
            print('No fuel!')
            print(error_to_fuel)
        else:
            self.con.commit()
            self.con.close()
