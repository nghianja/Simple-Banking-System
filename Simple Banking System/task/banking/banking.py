# Write your code here
import random


accounts = []
iin = "400000"


def check_account(card_number, pin_number):
    for account in accounts:
        if account[0] == card_number and account[1] == pin_number:
            return True
    return False


def check_card_number(card_number):
    for account in accounts:
        if account[0] == card_number:
            return True
    return False


def create_account():
    card_number = iin + f'{random.randint(0, 9999999999):010}'
    while check_card_number(card_number):
        card_number = f'{random.randint(0, 9999999999):010}'
    pin_number = f'{random.randint(0, 9999):04}'
    accounts.append([card_number, pin_number, 0])
    print("Your card has been created")
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin_number)
    print()


def print_balance(card_number):
    for account in accounts:
        if account[0] == card_number:
            print("Balance: " + account[2])


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
