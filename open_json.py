import json

def open_accounts():
    with open ("accounts.json", "r") as get_accounts:
        data = json.load(get_accounts)

    accounts = []

    for i in data['accounts']:
        accounts.append(i)


    account_names = []
    account_passwords = []

    for account in accounts:
        account_names.append(account['name'])
        account_passwords.append(account['password'])

    return account_names, account_passwords

open_accounts()
