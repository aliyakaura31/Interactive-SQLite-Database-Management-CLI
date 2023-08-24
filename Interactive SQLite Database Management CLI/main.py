import sqlite3

def databaseConnection(databaseName):
    try:
        conn = sqlite3.connect(f'{databaseName}.db')
        print(f"Database create with name : {databaseName}.db")
        conn.close()
    except Exception as e:
        print(e)



def createTable(databaseName, tableName, *fieldNames):
    try:
        conn = sqlite3.connect(f'{databaseName}.db')

        conn.execute(f'''CREATE TABLE {tableName} 
        ({fieldNames[0]} INT PRIMARY KEY NOT NULL,
        {fieldNames[1]} TEXT NOT NULL,
        {fieldNames[2]} TEXT NOT NULL,
        {fieldNames[3]} REAL NOT NULL)''')

        conn.close()
    except Exception as e:
        print(e)


def insertData(databaseName, tableName):
    try:
        conn = sqlite3.connect(f'{databaseName}.db')
        cursor = conn.execute(f"SELECT * FROM {tableName}")
        headings = [i[0] for i in cursor.description]
        empId = int(input("Enter your ID : "))
        empName = input("Enter your Name : ")
        empEmail = input("Enter your Email : ")
        empSalary = int(input("Enter your Salary : "))

        conn.execute(f"INSERT INTO {tableName} ({headings[0]}, {headings[1]}, {headings[2]}, {headings[3]}) \
                   VALUES (?, ?, ?, ?)", (empId, empName, empEmail, empSalary))

        conn.commit()
        print("Data inserted successfully")
        conn.close()
    except Exception as e :
        print(e)


def readData(databaseName, tableName):
    try:
        conn = sqlite3.connect(f'{databaseName}.db')
        cursor = conn.execute(f"SELECT * FROM {tableName}")
        getOption = int(input("Press 1. Get By ID 2. Fetch All : "))
        if getOption == 1:
            empId = int(input("Enter Your Id : "))
            for i in cursor:
                if i[0] == empId:
                    print("ID : ", i[0])
                    print("NAME : ", i[1])
                    print("EMAIL : ", i[2])
                    print("SALARY : ", i[3], "\n")

        elif getOption == 2:
            for i in cursor:
                print("ID : ", i[0])
                print("NAME : ", i[1])
                print("EMAIL : ", i[2])
                print("SALARY : ", i[3], "\n")

        else:
            print("Wrong Input")

        conn.close()
    except Exception as e :
        print(e)



def updateData(databaseName, tableName):
    try:
        conn = sqlite3.connect(f'{databaseName}.db')
        cursor = conn.execute(f"SELECT * FROM {tableName}")
        headings = [i[0] for i in cursor.description]
        condition = int(input("Press to Update 1. Name, 2. Email, 3. Salary : "))
        if condition == 1:
            empId = int(input("Enter your ID : "))
            empName = input("Enter your Name : ")
            conn.execute(f"UPDATE {tableName} set {headings[1]}={empName} WHERE {headings[0]}={empId}")
            conn.commit()

        elif condition == 2:
            empId = int(input("Enter your ID : "))
            empEmail = input("Enter your Email : ")
            conn.execute(f"UPDATE {tableName} set {headings[2]}={empEmail} WHERE {headings[0]}={empId}")
            conn.commit()

        elif condition == 3:
            empId = int(input("Enter your ID : "))
            empSalary = input("Enter your Salary : ")
            conn.execute(f"UPDATE {tableName} set {headings[3]}={empSalary} WHERE {headings[0]}={empId}")
            conn.commit()

        else:
            print("Wrong input")

        print("Data Updated")

        conn.close()
    except Exception as e :
        print(e)


def deleteData(databaseName, tableName):
    try:
        conn = sqlite3.connect(f'{databaseName}.db')
        cursor = conn.execute(f"SELECT * FROM {tableName}")
        headings = [i[0] for i in cursor.description]
        empId = int(input("Enter your ID : "))
        conn.execute(f"DELETE FROM {tableName} WHERE {headings[0]}={empId}")
        conn.commit()
        print("Data Deleted")

        conn.close()
    except Exception as e :
        print(e)

while True:
    displayMessage = "Press 1. For create New Database, 2. For Already existing Database, 3. Exit : "
    selectOption = int(input(displayMessage))

    if selectOption == 1:
        databaseName = input("Enter Your Database Name : ")
        databaseConnection(databaseName)

        while True:
            chooseOption = int(input("Press 1. Create Table, 2. Exit : "))
            if chooseOption == 1:
                tableName = input("Enter Your Table Name : ")
                fieldsName = []
                print("You can only insert 4 Headings..!!")
                for i in range(0, 4):
                    fieldName = input(f"Enter Your {i} heading : ")
                    fieldsName.append(fieldName)

                createTable(databaseName, tableName, *fieldsName)

            elif chooseOption == 2:
                break

            else:
                print("You Pressed Invalid Key...!!!")

    elif selectOption == 2:
        databaseName = input("Enter Your Database Name : ")

        while True:
            chooseOption = int(input("Press 1. Create New Table, 2. Access existing table, 3. Exit : "))
            if chooseOption == 1:
                tableName = input("Enter Your Table Name : ")
                fieldsName = []
                print("You can only insert 4 Headings..!!")
                for i in range(0, 4):
                    fieldName = input(f"Enter Your {i} heading : ")
                    fieldsName.append(fieldName)

                createTable(databaseName, tableName, *fieldsName)

            elif chooseOption == 2:
                tableName = input("Enter Your Table Name : ")
                while True:
                    operations = "Press 1. Insert Data, 2. Read Data, 3. Update Data, 4. Delete Data, 5. Exit : "
                    performOperation = int(input(operations))
                    if performOperation == 1:
                        insertData(databaseName, tableName)

                    elif performOperation == 2:
                        readData(databaseName, tableName)

                    elif performOperation == 3:
                        updateData(databaseName, tableName)

                    elif performOperation == 4:
                        deleteData(databaseName, tableName)

                    elif performOperation == 5:
                        break

                    else:
                        print("Invaild Option")

            elif chooseOption == 3:
                break

            else:
                print("You Pressed Invalid Key...!!!")

    elif selectOption == 3:
        print("Thank For Choosing Us..!!")
        break

    else:
        print("Invalid Input")
