#orders
"""
products = {}
while True:
    command = input()

    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        # update price and quantity
        products[name]["quantity"] += quantity
        products[name]["price"] = price

# print results
for name, data in products.items():
    total = data["price"] * data["quantity"]
    print(f"{name} -> {total:.2f}")

#parking lot
n = int(input())
parking = {}

for _ in range(n):
    parts = input().split()

    command = parts[0]
    username = parts[1]

    if command == "register":
        plate = parts[2]

        if username in parking:
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = plate
            print(f"{username} registered {plate} successfully")

    elif command == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

# print final registered users
for user, plate in parking.items():
    print(f"{user} => {plate}")

#courses
courses = {}

while True:
    line = input()
    if line == "end":
        break

    course, student = line.split(" : ")

    if course not in courses:
        courses[course] = []

    courses[course].append(student)

# Print results
for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for s in students:
        print(f"-- {s}")

#grades
n = int(input())

students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []

    students[name].append(grade)

# Filter and print only students with avg >= 4.50
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    if avg >= 4.50:
        print(f"{name} -> {avg:.2f}")


#companies
companies = {}

while True:
    line = input()
    if line == "End":
        break

    company, employee_id = line.split(" -> ")

    if company not in companies:
        companies[company] = []

    if employee_id not in companies[company]:
        companies[company].append(employee_id)

# Print results
for company, employees in companies.items():
    print(company)
    for emp in employees:
        print(f"-- {emp}")
"""