# Write your code here
import random
import sqlite3


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
iin = "400000"


def get_checksum(orig_number):
    int_number = [int(number) for number in orig_number]
    mul_number = [n * 2 if i % 2 == 0 else n for i, n in enumerate(int_number)]
    print(mul_number)
    sub_number = [n - 9 if n > 9 else n for i, n in enumerate(mul_number)]
    total = sum(sub_number)
    return str(((total + 9) // 10 * 10) - total)


def check_account(card_number, pin_number):
    if get_checksum(card_number[:-1]) == card_number[-1]:
        cur.execute("SELECT * FROM card WHERE number=? AND pin=?", (card_number, pin_number))
        rows = cur.fetchall()
        if rows:
            return True
    return False


def check_card_number(card_number):
    cur.execute("SELECT * FROM card WHERE number=?", (card_number,))
    rows = cur.fetchall()
    if rows:
        return True
    return False


def create_card_number():
    orig_number = iin + f'{random.randint(0, 999999999):09}'
    card_number = orig_number + get_checksum(orig_number)
    while check_card_number(card_number):
        orig_number = iin + f'{random.randint(0, 999999999):09}'
        card_number = orig_number + get_checksum(orig_number)
    return card_number


def create_account():
    card_number = create_card_number()
    pin_number = f'{random.randint(0, 9999):04}'
    cur.execute("INSERT INTO card(number, pin) VALUES (?, ?)", (card_number, pin_number))
    conn.commit()
    print("Your card has been created")
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin_number)
    print()


def print_balance(card_number):
    cur.execute("SELECT * FROM card WHERE number=?", (card_number,))
    row = cur.fetchone()
    print("Balance: " + row[2])


def login_account():
    print("Enter your card number:")
    card_number = input()
    print("Enter your PIN")
    pin_number = input()
    print()
    if check_account(card_number, pin_number):
        print("You have successfully logged in!")
        print()
        while True:
            print("1. Balance")
            print("2. Log out")
            print("0. Exit")
            command = int(input())
            print()
            if command == 0:
                return False
            if command == 1:
                print_balance(card_number)
            elif command == 2:
                print("You have successfully logged out!")
                break
    else:
        print("Wrong card number or PIN!")
    print()
    return True


if __name__ == "__main__":
    while True:
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        command = int(input())
        print()
        if command == 0:
            break
        if command == 1:
            create_account()
        elif command == 2:
            if login_account() is False:
                break
    print("Bye!")
    conn.close()
