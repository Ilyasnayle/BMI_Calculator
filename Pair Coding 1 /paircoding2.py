#Team Members

   # Ilyas Nayle
   # Ramadan Shemsu Hussen

#Question 1: Calculate the area and parameter of the Circle.

class circle:
    
    def __init__(self,radius):
        self.radius = radius
    
    def circle_area(self):
        return 3.143 * self.radius **2
    
    def circle_param(self):
        result = 2 * 3.14 * self.radius
        return result
    
    
radius = float(input("Enter the radius of the circle:"))
result = circle(radius)

print(f'\nArea of a circle is: {round(result.circle_area(),2)}')
print(f'Priemeter of the circle: {round(result.circle_param(),2)}')


#Question 2: Calculator
# Basic arithmatics: + - / * 

class calculator:
    
    def add(self, num1, num2):
        return print(num1 + num2)
    
    def sub(self, num1 , num2):
        return print(num1 - num2)
    
    def mul(self, num1, num2):
        return print(num1 * num2)
    
    def div(self, num1, num2):
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            return print(num1 / num2)
        
        
cal = calculator()
#getting user input: and performing the calculation based on the operatior sign

#q = "Quit"

while True:
    
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    operation = input("Please enter operation you want to perform: (+,-,/,*)")

    if operation == "+":
        addition = cal.add(num1,num2)
    elif operation == "-":
        substraction = cal.sub(num1,num2)
    elif operation =="/":
        division = cal.div(num1,num2)
    elif operation =="*":
        multiplication = cal.mul(num1,num2)
    else:
        print("Invalid operation: Please try again")
    
    
    choice = input("Do you wish to continue? (yes/no): ")
    if choice.lower() != 'Yes':
        break






#Question 3: Calculate the age or the person

class age:
    
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
        
    
    def cal_dob(self):
        dob_year, dob_month, dob_day = map(int, self.dob.split('-'))
        
        current_year = int(input("Enter the current year: "))
        
        age = current_year - dob_year
        
        return age
    
    

name = input("Enter your name please: ")
country = input("Enter your country please: ")
dob = input("Enter your date of birth as (YYYY-MM-DD): ")


person = age(name, country, dob)

print(f"Hello {person.name}, you are from {person.country}"
      f"and you are {person.cal_dob()} years old")



# Part 2 : Create the Databaes. 
import sqlite3


conn = sqlite3.connect('ecoles.db')

cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS eleves (
                    id INTEGER PRIMARY KEY,
                    nom TEXT,
                    prenom TEXT,
                    age INTEGER
                )''')

# Insert some sample data
cursor.execute("INSERT INTO eleves (nom, prenom, age) VALUES (?, ?, ?)", ('John', 'Doe', 20))
cursor.execute("INSERT INTO eleves (nom, prenom, age) VALUES (?, ?, ?)", ('Bob', 'Smith', 22))
cursor.execute("INSERT INTO eleves (nom, prenom, age) VALUES (?, ?, ?)", ('Bob', 'Johnson', 21))
cursor.execute("INSERT INTO eleves (nom, prenom, age) VALUES (?, ?, ?)", ('Emily', 'Jones', 23))
cursor.execute("INSERT INTO eleves (nom, prenom, age) VALUES (?, ?, ?)", ('James', 'Brown', 19))

conn.commit()

# Modify a record (Update)
cursor.execute("UPDATE eleves SET age = ? WHERE id = ?", (29, 2))  # Update John Doe's age to 25
conn.commit()


# Perform a query
cursor.execute("SELECT * FROM eleves")
rows = cursor.fetchall()
for row in rows:
    print(row)
    
