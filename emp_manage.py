import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Soham@2881"
)

cursor = con.cursor()

# CREATE DATABASE AND TABLE
cursor.execute("CREATE DATABASE IF NOT EXISTS Company")
cursor.execute("USE Company")
cursor.execute("""
     CREATE TABLE IF NOT EXISTS employes(
         id INT PRIMARY KEY,
         name VARCHAR(100),
         position VARCHAR(100),
         salary FLOAT
     )
""")
con.commit()

# CHECK FUNCTION
def check_employee(employee_id):
    sql = 'SELECT * FROM employes WHERE id = %s'
    cursor.execute(sql, (employee_id,))
    return cursor.fetchone() is not None

# ADD EMPLOYEE IF NOT EXISTS
def add_employee():
    Id = int(input("Enter Employee id : "))
    if check_employee(Id):
        print("Employee already exists.")
        return
    Name = input("Enter Employee name : ")
    Position = input("Enter Employee position in Company : ")
    Salary = float(input("Enter Employee salary : "))

    sql = 'INSERT INTO employes(id, name, position, salary) VALUES(%s, %s, %s, %s)'
    try:
        cursor.execute(sql, (Id, Name, Position, Salary))
        con.commit()
        print("Employee added successfully...")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# REMOVE EMPLOYEE
def remove_employee():
    id = int(input("Enter Employee id : "))
    if not check_employee(id):
        print("Employee does not exist.")    
        return

    sql = 'DELETE FROM employes WHERE id = %s'
    try:
        cursor.execute(sql, (id,))
        con.commit()
        print("Employee successfully deleted...")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# PROMOTE EMPLOYEE
def promote_employee():
    id = int(input("Enter Employee id : "))
    if not check_employee(id):
        print("Employee does not exist.") 
        return

    Amount = float(input("Enter salary increase : "))
    sql = 'SELECT salary FROM employes WHERE id = %s'
    cursor.execute(sql, (id,))
    current_salary = cursor.fetchone()[0]
    new_salary = current_salary + Amount
    cursor.execute('UPDATE employes SET salary = %s WHERE id = %s', (new_salary, id))
    con.commit()
    print("Employee promoted successfully...")

# DISPLAY EMPLOYEES
def display_employee():
    cursor.execute('SELECT * FROM employes')
    results = cursor.fetchall()
    if not results:
        print("No employees found.")
    else:
        for emp in results:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Post: {emp[2]}, Salary: {emp[3]}")
            print("-" * 40)

# MENU
def menu():
    while True:
        print("\n_________ Employee Management Menu _________")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Promote Employee")
        print("4. Display All Employees")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            remove_employee()
        elif choice == '3':
            promote_employee()
        elif choice == '4':
            display_employee()
        elif choice == '5':
            print("Goodbye!!")
            break
        else:
            print("Invalid input, try again")

# RUN
if __name__ == "__main__":
    menu()
