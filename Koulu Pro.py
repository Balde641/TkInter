# Creating a login function
from tkinter import *
import sqlite3, time

def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome "+i[2])
            #return("exit")
            break

        else:
            print("Username and password not recognised")
            again = input("Do you want to try again?(y/n: ")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                #return("exit") 
                break           

login()

# Create new user funtion
def newUser():
    found = 0
    while found == 0:
        username = input("Please enter a username: ")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(findUser, [{username}])

        if cursor.fetchall():
            print("User name Take, please try again") 
        else:
            found = 1

    firstName = input("Enter your first name: ") 
    surname = input("Enter your surname: ")
    password = input("Please enter your password: ")
    password1 = input("Please reenter your password: ") 

    while password != password1:
        print("Your password didn't match, plese try again") 
        password = input("Please enter your password: ")
        password1 = input("Please reenter your password: ") 

    insetData = '''INSERT INTO user(username,firstname,surname,password
    VALUES(?,?,?,?)'''

    cursor.execute(insetData,[(username),(firstName),(surname),(password)])
    db.commit()
              
newUser()



