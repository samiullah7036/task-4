employees = [
    {"name": "John", "age": 25, "role": "Developer", "salary": 50000},
    {"name": "Sara", "age": 28, "role": "Manager", "salary": 70000}
]

# Show employees
for e in employees:
    print(e)

# Update John role
employees[0]["role"] = "Senior Developer"

# Delete Sara
employees.pop(1)

print("\nAfter Update & Delete:\n")

# Show again
for e in employees:
    print(e)
    student = {
    "name": "John",
    "marks1": 80,
    "marks2": 70,
    "marks3": 60
}

# Calculate total and average
total = student["marks1"] + student["marks2"] + student["marks3"]
average = total / 3

# Grade
if average >= 80:
    grade = "A"
elif average >= 50:
    grade = "B"
else:
    grade = "C"

# Display report
print("Report Card")
print("Name:", student["name"])
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
cart = [
    {"name": "Pen", "price": 10, "qty": 2},
    {"name": "Book", "price": 50, "qty": 1}
]

# Display items
print("Cart Items:")
total = 0

for item in cart:
    print(item)
    total += item["price"] * item["qty"]

print("Total Bill:", total)

# Remove item (Book)
for item in cart:
    if item["name"] == "Book":
        cart.remove(item)

print("\nAfter Removing Book:\n")

# Display again
total = 0
for item in cart:
    print(item)
    total += item["price"] * item["qty"]

print("Total Bill:", total)
users = {
    "admin": "1234",
    "john": "pass"
}

# Take input
username = input("Enter username: ")
password = input("Enter password: ")

# Validate
if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Login Failed")
    visitors = set()

# Add visitors
visitors.add("John")
visitors.add("Sara")
visitors.add("John")   # duplicate
visitors.add("Mike")

# Display visitors
print("Visitors:", visitors)

print("Total unique visitors:", len(visitors))

# Input
name = input("Enter name: ")
product = input("Enter product: ")

# Formatted sentence
print(f"{name} bought {product}")

# Padding
print("Left  :", name.ljust(10))
print("Right :", name.rjust(10))
print("Center:", name.center(10))
account = {"name": "John", "balance": 1000}

# Deposit
account["balance"] += 500

# Withdraw
account["balance"] -= 200

# Show balance
print(account)
votes = {"A": 0, "B": 0, "C": 0}

# Add votes
votes["A"] += 1
votes["B"] += 2
votes["C"] += 1

# Display votes
print("Votes:", votes)

# Find winner
winner = max(votes, key=votes.get)
print("Winner:", winner)
students = {
    "John": ["Math", "Science"],
    "Sara": ["English"]
}

# Add student
students["Mike"] = ["Physics", "Chemistry"]

# Update courses
students["John"].append("Computer")

# Display students
print(students)
num = 1000

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hex:", hex(num))

print("Comma format:", f"{num:,}")
print("Scientific:", f"{num:e}")