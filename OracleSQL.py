import os
import subprocess as sp
import json
import sys

json_file = open("settings.json", "r")
settings = json.load(json_file)
json_file.close()
accounts = settings["accounts"]
script_dir = settings["script_dir"]
password = settings["password"]
json_file = open("settings.json", "w")

try:
    os.chdir(script_dir)
except FileNotFoundError:
    print("\nYour script directory path doesn't exist!\n")
runFlag = True

def change_settings():
    setting_choice = int(input("\nWhat would you like to do? \nCommands:\n1)Change accounts\n2)Change script dir path\n3)Quit\n>"))
    if setting_choice == 1:
        normal_account = input("\nWhat is your username for your normal account?\n>")
        course_account = input("\nWhat is your username for your coursework account?\n>")
        new_password = input("\nWhat is the password for these accounts (This should be your student ID)\n>")
        settings["accounts"] = [normal_account, course_account]
        settings["password"] = new_password
        json.dump(settings, json_file)
    elif setting_choice == 2:
        new_dir = input("\nWhat is the path to your script directory?\n>")
        settings["script_dir"] = new_dir
        json.dump(settings, json_file)
    else:
        if setting_choice != 3:
            print("\nIncorrect input!\n")
            print("Returning to homepage...")

while runFlag:
    account_choice = int(input("\nWhich account would you like to log into?\n1)Normal\n2)Coursework\n3)Change Settings\n4)Quit\n>"))

    if (account_choice == 1 or account_choice == 2):
        runFlag = False

    elif (account_choice == 3):
        change_settings()
    elif (account_choice == 4):
        json.dump(settings, json_file)
        json_file.close()
        quit()
    else:
        print("\nIncorrect Input\n")
        input("Press Enter to continue...\n")   
        

files = [f for f in os.listdir(".") if os.path.isfile(f)]
runFlag = True

while runFlag:
    os.chdir(script_dir)
    print("\n")
    print("\nHere are your available scripts:\n")
    for i in range(0,len(files)):
        print(files[i][:len(files[i])-4])

    choice = input("\nWhat would you like to do? \nform: 'command file'\n\nCommands:\nedit\nedit folder (open scripts folder)\nrun\nquit\n> ")

    if (choice == "quit"):
        runFlag = False
        json.dump(settings, json_file)
        json_file.close()
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
        run_time = ""
        
        run_time = sp.Popen(f"sqlplus.exe {accounts[account_choice-1]}@student/{password}", stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)
        s = run_time.communicate(f"@{script_dir}{current_file}.sql\n".encode())[0].decode()
        s = s[s.find("options")+15:]
        s = s[:s.find("SQL>")]
        print("\n"+s)
        input("Press Enter to continue...\n")
    else:
        print("\nIncorrect Input\n")
        input("Press Enter to continue...\n")