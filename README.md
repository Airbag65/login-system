# login-system
This is a login system that I made with python. 
The information about the different accounts and their passwords are stored in the .json file. 
This little project was my first time working with JSON so it was firstly just ment to be a small thing to learn the basics, 
but it turned into something I genuinly think can be useful. 
It could be implemented as a login system for a larger problem. 
I will also add a way to sign up more accounts from the commandline in the future. 

### login.py
The login.py file contains all the code that does the actual logging in. 
It gives the user the posibility to choose which account to log into and handles all comparisons to make sure 
that the passwords match up to the selected account. 
The login.py script does also include the posibility to create new accounts, but the functionality 
comes from the add_account.py script.

### open_json.py 
The open_json.py file opens the accounts.json file, gets the data from it and converts it 
into something the login.py script is able to use for the identification. It stores the names and passwords in two 
arrays in which the indices match up. For example the first name in the names array corresponds to the first password 
in the passwords array. 

### accounts.json
The accounts.json file just simply stores the names and the passwords in separate objects that 
work as accounts. Serves no other purpose than Storing information about the different 
accounts.

### add_account.py
The add_account.py file handles the functionality of creating new accounts. 
A summary of what it's doing is as follows: opens the JSON file and stores it's data in an array of dicts, 
asks the user for input for a new account to be created and stores the inputed data in a new dict varible 
following the same layout as the JSON file, appends the new dict to the array of dicts and then lastly overwrites 
the existing JSON data with the new array containing all the old accounts and the new one.

### Update 2 Feb 2021
The functionality to add new accounts has now also been implemented. 
The source code for that can be found in the add_account.py file.
For the entire program to run, you just simply run the login.py file and all the other files should be connected. 

### Update 10 Feb 2021
I have now found a way to put this to use. I have created a script with this as it's fundamentals for 
logging in and selecting the active account. The script is a way to send emails without having to open a browser. 
The user does simply login to their account which has their email information linked to it. The text of the email is stored in 
a .txt file separate to the script. In this way, the user can take all the time they need to think about what to type in the mail before sending 
since the UI is just a textfile and not the mail interface, which can for some invoke stress. The source code can be found in its own repo.
Just as a sidenote however, I am very well aware that 
such a thing is totally unecessary but I thought it was a fun thing to work on. 
