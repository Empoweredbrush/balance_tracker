import sqlite3

conn = sqlite3.connect("balance_tracker.db")

print("Connected successfully!")

"""
conn.execute('''CREATE TABLE EXPENSES
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AMOUNT          DECIMAL(65, 2)    NOT NULL,
         DESCRIPTION     CHAR(50));''')

print("Created Table Successfully!")
"""


def Start():
    print("Welcome to your balance tracker! This program was created to help you in tracking your balance and expenses.")
    print("To start will you be adding a new expense, updating an expense, deleting an expense, or looking for an expense? (use A for new, B for update, C for delete, and D for viewing one expense):")

    answer = input()

    if (answer.lower() == "a"):
       Add()
    
    if (answer.lower() == "b"):
        Update()
    
    if (answer.lower() == "c"):
        Delete()
    
    if (answer.lower() == "d"):
        View()

def Add():
    print("Welcome to the add part of the program! We will be adding a new expense to your tracker but need some info.")
    idList = []

    cur = conn.cursor()

    cur.execute('''SELECT ID FROM EXPENSES''')
    rows = cur.fetchall()

    for row in rows:
        idList.append(row)

    length = len(idList)

    if length == 0:
        id = 1
    if length  >= 1:
        id = length + 1
    

    print("To start, please give the name of the expense:")

    name = input()

    print("Now, please put down the amount (Note, after the decimal max of two numbers, Example: 2.50):")

    number = input()
    amount = float(number)

    print("Next, add a very very short description, 50 character limit, or type no to leave blank:")

    answer = input()

    description = None

    if (answer.lower() != "no"):
        description = answer
    
    conn.execute('''INSERT INTO EXPENSES (ID, NAME, AMOUNT, DESCRIPTION)
                 VALUES (?, ?, ?, ?)''', (id, name, amount, description))

    conn.close()

def Update():
    print("To begin updating your Balance Tracker entry, please give the name of the expense you wish to update(Note: is case sensitive):")
    name = input()

    print("With that expense what are you updating? (A for name, b for expense amount, c for description):")
    response = input()
    answer = response.lower()

    if answer == "a":
        newName = input("What is the new name of the expense?")

        conn.execute('''UPDATE EXPENSES SET NAME = (?) WHERE NAME = (?)''', (newName, name))
        conn.close()

    if answer == "b":
        newAmount = input("What is the new amount:")
        conn.execute('''UPDATE EXPENSES SET AMOUNT = (?) WHERE NAME = (?)''', (newAmount, name))
        conn.close()

    if answer == "c":
        newDesc = input("What is the new description(50 character limit)")
        conn.execute('''UPDATE EXPENSES SET DESCRIPTION = (?) WHERE NAME = (?)''', (newDesc, name))
        conn.close()


def Delete():
    entry = input("What is the expense name you wish to delete(Note case sensitive):")

    conn.execute('''DELETE FROM EXPENSES WHERE NAME = (?)''', (entry))

def View():


    print("What is the expense are you looking for? (Note: case sensitive):")

    item = input()

    conn.execute('''SELECT NAME, AMOUNT, DESCRIPTION FROM EXPENSES WHERE NAME = (?)''', (item))

    conn.close()



Start()