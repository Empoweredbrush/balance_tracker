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

    #if (answer.lower() == "a"):
       # Add()

def Add():
    print("Welcome to the add part of the program! We will be adding a new expense to your tracker but need some info.")
    idList = []

    cur = conn.cursor()

    cur.execute('''SELECT ID FROM EXPENSES''')
    rows = cur.fetchall()

    for row in rows:
        idList.append(row)
    
    item = idList[-1]

    id = 1 + int(item)

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
                 VALUES ({id}, {name}, {amount}, {description})''')

    conn.close()

#def Update():

#def Delete():

#def View():