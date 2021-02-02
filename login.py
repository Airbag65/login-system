from time import sleep
import json
import open_json
import add_account

# Booleans
logged_in = False
account_found = False

# Strings
password = "snöboll"
chosen_account = ""
active_password = ""
compared_account = ""
user_choice = ""

# Integers
num = -1

# Imported arrays from open_json.py
available_accounts = open_json.open_accounts()[0]
possible_passwords = open_json.open_accounts()[1]


def choose_account():
    global available_accounts, chosen_account, compared_account, possible_passwords, active_password, num, account_found

    num = -1
    print("\nAvailable accounts: ")
    for i in available_accounts:
        print(i)
    print("")
    chosen_account = input("Type the name of the account you want to log into: ")
    for i in available_accounts:
        num += 1
        if chosen_account.lower() == i.lower():
            chosen_account = i
            active_password = possible_passwords[num]
            account_found = True
            print("Account Found!\nEnter the password for " + chosen_account + "\n")
        else:
            account_found = False

        if account_found:
            break
        else:
            continue
    if account_found == False:
        print("\nAccound not Found!\nTry Again!")


def logging_in():
    global logged_in
    global active_password
    user_input = input("Password: ")
    if user_input == active_password:
        logged_in = True
        print("\nLogging in...\n")
        sleep(.5)
    else:
        print("\nPassword was incorrect\nTry again\n")
        sleep(.5)


def system():
    print("\nWelcome! \n")


def run():
    global logged_in, chosen_account, account_found, user_choice

    user_choice = input("Do you want to log into an existing account or create a new account? [L/C]: ")
    if user_choice.lower() == 'l':
        print("")
    elif user_choice.lower() == 'c':
        add_account.create_account()

    while account_found == False:
        choose_account()
    while logged_in == False:
        logging_in()
    if logged_in:
        system()

run()
