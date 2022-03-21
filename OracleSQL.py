import os
import subprocess as sp
from time import sleep

accounts = ["username", "username"]
os.chdir("C://Users/joshu/Documents/Uni/CSY1026/scripts/")
runFlag = True

while runFlag:
    account_choice = int(input("\nWhich account would you like to log into?\n1) Normal\n2) Coursework\n>"))

    if (account_choice == 1 or account_choice == 2):
        runFlag = False
    else:
        print("\nIncorrect Input\n")
        input("Press Enter to continue...\n")   
        

print("\nHere are your available scripts:\n")
files = [f for f in os.listdir(".") if os.path.isfile(f)]
runFlag = True

while runFlag:
    os.chdir("C://Users/joshu/Documents/Uni/CSY1026/scripts/")
    for i in range(0,len(files)):
        print(files[i][:len(files[i])-4])

    choice = input("\nWhat would you like to do? \nform: 'command file'\n\nCommands:\nedit\nedit folder\nrun\nquit\n> ")

    if (choice == "quit"):
        runFlag = False
        break
    try:
        split_choice = choice.rsplit(" ",1)
        command = split_choice[0]
        current_file = split_choice[1]
    except IndexError:
        print ("\nIncorrect Input\n")
        input("Press Enter to continue...\n")   
        continue

    if (command == "edit"):
        if (current_file == "folder"):
            os.system("code --n .")
        else:
            os.system(f"code {current_file}.sql")

    elif (command == "run"):
        os.chdir("C://Oracle12c/")
        run_time = sp.Popen(f"sqlplus.exe {accounts[account_choice-1]}@student/password", stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)
        print("\n"+run_time.communicate(f"@C://Users/joshu/Documents/Uni/CSY1026/scripts/{current_file}.sql\n".encode())[0].decode())
        input("Press Enter to continue...\n")
    else:
        print("\nIncorrect Input\n")
        input("Press Enter to continue...\n")
