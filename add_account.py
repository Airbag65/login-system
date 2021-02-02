import json

# Strings
name = ""
password = ""
# Confirmation needs to be different from beginning for program to run
confirm_password = "1"

# Dictionary for new account
new_account = {}


def create_account():
    global name, password, confirm_password, new_account
    name = input(
        "Select the name of the new account. \nMake sure to double check if it's correct before submiting! \nEnter the name of the account: "
        )
    create_password()
    if password != confirm_password:
        print("\nThe passwords do not match!\nTry again!\n")
        create_password()
    new_account = {'name': f'{name}','password': f'{password}'}

    with open ("accounts.json", "r") as open_file:
        data = json.load(open_file)
        open_file.close()

    data['accounts'].append(new_account)

    write_file = open("accounts.json", "w+")
    write_file.write(json.dumps(data, indent = 4, sort_keys = True))
    write_file.close()
    

def create_password():
    global password, confirm_password
    password = input("\nSelect a password for the new account.\nEnter new password: ")  
    confirm_password = input("Please confirm the password: ")
