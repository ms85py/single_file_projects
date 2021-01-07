import random
import sqlite3


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

# cur.execute('DROP TABLE card')

cur.executescript('''
CREATE TABLE IF NOT EXISTS card (
id INTEGER PRIMARY KEY AUTOINCREMENT,
number TEXT,
pin TEXT,
balance INTEGER DEFAULT 0
);
''')


def create_account(card_id, pin):
    print(f"""
Your card has been created.
Your card number:
{card_id}
Your card PIN:
{pin}
""")
    cur.execute('INSERT INTO card (number, pin) VALUES (?, ?)', (card_id, pin))
    conn.commit()


class BankingSystem:
    def __init__(self, comm, session_id, iin):
        self.comm = comm
        self.session_id = session_id
        self.iin = iin


    def menu1(self):
        while self.comm != 0:
            self.comm = int(input("""
    1. Create an account
    2. Log into account
    0. Exit
    """))
            if self.comm == 1:
                self.card_gen()
            elif self.comm == 2:
                self.login()
            elif self.comm == 0:
                break


    def menu2(self):
        while self.comm != 0:
            self.comm = int(input("""
    1. Balance
    2. Add income
    3. Do transfer
    4. Close account
    5. Log out
    0. Exit
    """))
            if self.comm == 1:
                self.get_balance()
            elif self.comm == 2:
                self.add_income()
            elif self.comm == 3:
                self.transfer()
            elif self.comm == 4:
                self.close_account()
            elif self.comm == 5:
                self.session_id = ""
                self.menu1()
            elif self.comm == 0:
                break


    def transfer(self):
        print("Transfer\n")
        c_to_trans_to = input("Enter card number:\n")
        self.luhn(card_id=c_to_trans_to, to_do="check")


    def card_exist_check(self, card_num):
        cur.execute('SELECT number FROM card WHERE number=?', (card_num,))
        exist_check = cur.fetchone()
        if exist_check is None:
            print("Such a card does not exist.\n")
            self.menu2()
        else:
            self.do_transfer(card=card_num)


    def do_transfer(self, card):
        if card == self.session_id:
            print("You can't transfer money to the same account!")
        else:
            money_to_trans = int(input("Enter how much money you want to transfer:\n"))
            cur.execute('SELECT balance FROM card WHERE number=?', (self.session_id,))
            curr_balance = cur.fetchone()
            if curr_balance[0] < money_to_trans:
                print("Not enough money!")
            else:
                cur.execute('UPDATE card SET balance = balance - ? WHERE number=?', (money_to_trans, self.session_id))
                cur.execute('UPDATE card SET balance = balance + ? WHERE number =?', (money_to_trans, card))
                conn.commit()
                print("Success!")


    def add_income(self):
        to_add = input("Enter income:\n")
        cur.execute('UPDATE card SET balance = balance + ? WHERE number=?', (to_add, self.session_id))
        conn.commit()
        print("Income was added!")


    def close_account(self):
        cur.execute('DELETE FROM card WHERE number=?', (self.session_id,))
        conn.commit()
        print("The account has been closed!")
        self.session_id = ""
        self.menu1()


    def get_balance(self):
        cur.execute('SELECT balance FROM card WHERE number=?', (self.session_id,))
        balance = cur.fetchone()
        print(f"Balance: {balance[0]}")

    def card_gen(self):
        card_id = ""
        card_id += str(self.iin)
        for i in range(10):
            card_id += str(random.randint(0, 9))
        self.luhn(card_id=card_id, to_do="create")


    def luhn(self, card_id, to_do):
        odd_as_int = [int(x) for x in card_id[::-2]]
        even_as_int = [int(x) for x in card_id[-2::-2]]
        total1 = 0
        total2 = 0
        for x in even_as_int:
            if (x * 2) > 9:
                total1 += ((x * 2) - 9)
            else:
                total1 += x * 2

        for y in odd_as_int:
            total2 += y

        if to_do == "create":
            if (total1 + total2) % 10 == 0:
                self.create_pin(card_id=int(card_id))
            else:
                self.card_gen()

        elif to_do == "check":
            if (total1 + total2) % 10 == 0:
                self.card_exist_check(card_num=card_id)
            else:
                print("You probably made mistake when entering the card number. Please try again!")
                self.menu2()


    def create_pin(self, card_id):
        new_pin = ""
        cur.execute('SELECT number FROM card')
        cards = cur.fetchall()
        if card_id not in cards:
            for i in range(4):
                new_pin += str(random.randint(0, 9))
            create_account(card_id=card_id, pin=new_pin)
        else:
            self.card_gen()


    def login(self):
        card_id = input("Enter your card number:\n")
        in_pin = input("Enter your PIN:\n")
        cur.execute('SELECT pin FROM card WHERE number=?', (card_id,))
        pin_to_test = cur.fetchone()
        if pin_to_test is not None:
            if in_pin == pin_to_test[0]:
                print("You have successfully logged in!")
                self.session_id = card_id
                self.menu2()
            else:
                print("Wrong card number or PIN")
        elif pin_to_test is None :
            print("Wrong card number or PIN!")
            self.menu1()


if __name__ == "__main__":
    instance = BankingSystem("_", "_", 400000)
    instance.menu1()