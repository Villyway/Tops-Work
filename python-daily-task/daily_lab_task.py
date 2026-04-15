                                               #  --------------     Daily Lab Task     ------------------------  #

# 20th March
# Task 1 : Perform arithmetic operations (+, -, *, /) on float values.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


#______________________________________________________

# 23rd March
# Lab Task in class : Accept 2 numbers first base and second power and print answer.

base=int(input("Enter base value"))
power = int(input("Enter power value"))
ans = base**power

print(f"this is the result {base**power}")
print(f"this is the result {ans}")

# Lab Task in class : floor division (//) and modulus (%) on two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

floor_div = num1 // num2
print("Floor value : ", floor_div)

mod = num1 % num2
print("Modulus value : ", mod)


# Task 1 : Accept a number and check if it is divisible by 5.

num = int(input("Enter number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# Task 2 : Calculate Simple Interest.

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
n = float(input("Enter time: "))
si = (p * r * n) / 100
print("Simple Interest:", si)

# Task 3 : Convert Celsius to Fahrenheit.

c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)

# Task 4 : Accept radius and find area of circle.

r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area of circle:", area)

#______________________________________________________

# 25th March
# Task : Perform all assignment operators in a single program.

a = 10

a += 5
print("After += :", a)

a -= 3
print("After -= :", a)

a *= 2
print("After *= :", a)

a /= 4
print("After /= :", a)

#______________________________________________________

# 27th March
# Task 1 : Create grading program using match case.

marks = int(input("Enter marks: "))

match marks // 10:
    case 10 | 9 | 8 | 7:
        print("Grade A")
    case 6:
        print("Grade B")
    case 5:
        print("Grade C")
    case _:
        print("Fail")

# Task 2 : Check leap year.

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# Task 3 : Check number divisible by 5 and 7.

num = int(input("Enter number: "))
if num % 5 == 0 and num % 7 == 0:
    print("Divisible by both 5 and 7")
else:
    print("Not divisible")

#______________________________________________________

# 28th March
# Task : Convert for loop into while loop.

i = 1
while i <= 5:
    print(i)
    i += 1

#______________________________________________________

# 31st March
# Task 1 : Check prime number using for loop.

num = int(input("Enter number: "))
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    if num > 1:
        print("Prime")
    else:
        print("Not Prime")

# Task 2 : Find sum of first 100 even numbers.

sum = 0
for i in range(2, 201, 2):
    sum += i
print("Sum:", sum)

# Task 3 : Find sum of numbers divisible by 5 and 7 between 1000–2000.

sum = 0
for i in range(1000, 2001):
    if i % 5 == 0 and i % 7 == 0:
        sum += i
print("Sum:", sum)

#______________________________________________________

# 1st April
# Task 1 : Find sum of digits.

num = int(input("Enter number: "))
sum = 0

while num > 0:
    rem = num % 10
    sum += rem
    num //= 10

print("Sum of digits:", sum)


# Task 2 : Count even and odd digits.
# num = int(input("Enter number: "))

even = 0
odd = 0

while num > 0:
    rem = num % 10
    if rem % 2 == 0:
        even += 1
    else:
        odd += 1
    num //= 10

print("Even digits:", even)
print("Odd digits:", odd)

#______________________________________________________


# 2nd April
# Task : Pattern program

n = int(input("Enter number: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

#______________________________________________________


# 3rd April
# Task : Find length of each word in string

text = input("Enter sentence: ")
words = text.split()

for w in words:
    print(w, len(w))

#______________________________________________________


# 4th April
# Task : String method checks

s = input("Enter string: ")

print(s.isdigit())
print(s.isalpha())
print(s.isalnum())

#______________________________________________________


# 6th April
# Task : Negative slicing

name = input("Enter name: ")

print(name[::-1])

#______________________________________________________


# 8th April

# Task 1. count each city in list

lst_city = ['ahmedabad','surat','rajkot','surat','dahod','daman','dahod']
for i in range(len(lst_city)):
    if lst_city[i] in lst_city[:i]:
        continue
    
    count = 0
    for j in lst_city:
        
        if lst_city[i] == j:
            count += 1
    print(lst_city[i], count)
    
    
# Task 2. count no of vowels in each city
vowels = ['a','A','E','e','i','I','o','O','U','u']
count=0
lst_city = ['ahmedabad','surat','rajkot']
for i in lst_city:
    count=0
    for j in i:
        if j in vowels:
            count+=1
    print(i,count)

# Task 3. menu-driven shopping list
shopping_list = []
while True:
    print("\nShopping List Menu")
    print("1. Add Item\n2. Update Item\n3. Delete Item\n4. Search Item\n5. View List\n6. Exit")

    choice = input("Enter choice: ")
    if choice == '1':
        item = input("Enter item you want to add: ")

        if item in shopping_list:
            print("Item already exists in shopping list")
        else:
            shopping_list.append(item)
            print(f"{item} added successfully")

    elif choice == '2':
        old = input("Which item you want to update: ")
        if old in shopping_list:
            new = input("Enter new item: ")
            index = shopping_list.index(old)
            shopping_list[index] = new
            print("Item Updated successfully")
        else:
            print("Item is not available for update")

    elif choice == '3':
        item = input("Enter item to delete: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("Item is deleted")
        else:
            print("Item unavailable")

    elif choice == '4':
        item = input("which item you want to search: ")
        if item in shopping_list:
            print(f"{item} is available")
        else:
            print(f"{item} is unavailable")

    elif choice == '5':
        print("Your Shopping List:", shopping_list)

    elif choice == '6':
        print("Exit")
        break

    else:
        print("Invalid choice")

#______________________________________________________

# 9th April
# Task : Name Pattern Program

name=input("Enter your name : ")
print(name)
for i in range(len(name)):
    for j in range(i+1):
        print(name[j],end=" ")
    print()
#______________________________________________________


# 11th April
# Task : Student total marks

students = {
    "Ramesh": [100, 100, 100],
    "Riya": [80, 70, 80]
}

for k, v in students.items():
    print(k, sum(v))

#______________________________________________________
# 13th April
# Task : Menu Driven program for employees using dictionary


emp_data={
    101:{"name":"rahul","email":"rahul@gmail.com","salary":"21000","city":"ahmedabad"},
    102:{"name":"mahesh","email":"mahesh@gmail.com","salary":"18000","city":"baroda"},
    103:{"name":"riya","email":"riya@gmail.com","salary":"23000","city":"surat"},
    104:{"name":"mehul","email":"mehul@gmail.com","salary":"19800","city":"rajkot"},
}

while True:
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Update Employee")
    print("4. Show Employees")
    print("5. Search by Salary")
    print("6. Search by City")
    print("7. Delete Employee")
    print("8 Exit")
    choice = int(input("Enter Choice : "))
    match choice:
        case 1:
            eid=int(input("Enter eid : "))
            ename= input("Enter name : ")
            email= input("Enter email : ")
            salary= input("Enter salary : ")
            city= input("Enter city : ")
            emp_data[eid]={"name":ename,"email":email,"salary":salary,"city":city}
            print("Employee added Successfully")
        case 2:
            search_id=int(input("Enter emp_id : "))
            if search_id in emp_data.keys():
                print(emp_data[search_id])
            else:
                print(f"{search_id} is not exist")
        case 3:
            search_id=int(input("Enter emp_id : "))
            if search_id in emp_data.keys():
                new_salary=input("Enter updated salary : ")
                emp_data[search_id]["salary"] = new_salary
        case 4:
            for k,v in emp_data.items():
                print(k)
                for k1,v1 in v.items():
                    print("\t",v1)
        case 5:
            e_salary=input("Enter salary to search : ")
            for emp_id,details in emp_data.items():
                if details["salary"]==e_salary:
                    print(emp_id,details)
                    break
            else:
                print(f"{e_salary} is not exist")
        case 6:
            e_city = input("Enter city to search : ")
            for emp_id,details in emp_data.items():
                if details['city']==e_city:
                    print(emp_id,details)
                    break
            else:
                print(f"{e_city} Not found")
        case 7:
            delete_emp = int(input("Enter emp_id to delete : "))
            if delete_emp in emp_data.keys():
                del emp_data[delete_emp]
                print(f"{delete_emp} deleted")
                
            else:
                print(f"{delete_emp} Not found")        
        case 8:
            break


#______________________________________________________


# 14th April
# Task 1 : Create Function to check given number is positive or negative

def check(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
        
num = int(input("Enter number : "))
check(num)

# Task 2 : Create Function to check given number is prime or not

def prime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

num = int(input("Enter number: "))
result = prime(num)
print(result)

# Task 3 : Car Data Menu Driven Program

car_data = {
    "EV": {
        "Hundai": {
            "i10": {"price": 800000, "model": "EV-i10"},
            "Creta": {"price": 1500000, "model": "EV-Creta"}
        },
        "TATA": {
            "Nexon": {"price": 1400000, "model": "EV-Nexon"},
            "Harrier": {"price": 2000000, "model": "EV-Harrier"}
        }
    },
    "Petrol": {
        "Hundai": {
            "i10": {"price": 700000, "model": "Petrol-i10"},
            "Creta": {"price": 1400000, "model": "Petrol-Creta"},
            "i20": {"price": 900000, "model": "Petrol-i20"}
        },
        "Maruti": {
            "Baleno": {"price": 800000, "model": "Petrol-Baleno"},
            "Swift": {"price": 700000, "model": "Petrol-Swift"},
            "Breeza": {"price": 1100000, "model": "Petrol-Breeza"}
        }
    },
    "Diesel": {
        "Hundai": {
            "i10": {"price": 850000, "model": "Diesel-i10"},
            "Creta": {"price": 1600000, "model": "Diesel-Creta"},
            "i20": {"price": 950000, "model": "Diesel-i20"}
        },
        "Maruti": {
            "Baleno": {"price": 850000, "model": "Diesel-Baleno"},
            "Swift": {"price": 750000, "model": "Diesel-Swift"},
            "Breeza": {"price": 1200000, "model": "Diesel-Breeza"}
        }
    }
}


while True:
    print("\n====== CAR MENU ======")
    print("1. See EV Cars")
    print("2. See Maruti Cars")
    print("3. See Swift Details")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("\n--- EV Cars ---")
        for brand, cars in car_data["EV"].items():
            print(f"\n{brand}:")
            for car, details in cars.items():
                print(f"  {car} -> Price: {details['price']}, Model: {details['model']}")

    elif ch == 2:
        print("\nAvailable Maruti Cars:")
        for car in car_data["Petrol"]["Maruti"]:
            print(car)

        car_name = input("Enter car name: ").capitalize()

        if car_name in car_data["Petrol"]["Maruti"]:
            print("\nPetrol Details:", car_data["Petrol"]["Maruti"][car_name])
        if car_name in car_data["Diesel"]["Maruti"]:
            print("Diesel Details:", car_data["Diesel"]["Maruti"][car_name])

        if car_name not in car_data["Petrol"]["Maruti"]:
            print("Car not found")

    elif ch == 3:
        fuel = input("Enter fuel type (Petrol/Diesel): ").capitalize()

        if fuel in car_data:
            print("\nSwift Details:")
            print(car_data[fuel]["Maruti"]["Swift"])
        else:
            print("Invalid fuel type")

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

#______________________________________________________

# 15th April
# Task 1 : Square function

def square(n):
    return n * n

num = int(input("Enter number: "))
ans = square(num)
print("Square:", ans)

# Task  2 : Write python function to Merge Two List

def mergeList(list_a,list_b):
    return list_a + list_b
    
list_a=[1,2,3]
list_b=[4,5,6]

result=(mergeList(list_a,list_b))
print(result)

# Task  3 : Write python function to Merge Two dictionary

def mergeDict(dict_a, dict_b):
    result = {}
    for key in dict_a:
        result[key] = dict_a[key]
    for key in dict_b:
        result[key] = dict_b[key]
    return result

dict_a = {"name": "aman", "age": 21}
dict_b = {"city": "rajkot"}

ans = mergeDict(dict_a, dict_b)
print(ans)
