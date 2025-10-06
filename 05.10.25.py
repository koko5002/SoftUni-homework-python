'''#zad1
inpu=input()
def abs_value(input1):
    numbers=input1.split(" ")
    absValues = []
    for i in numbers:
        absValues.append(abs(float(i)))
    print(absValues)

abs_value(inpu)

#zad2
def grades(grade):
    if 2.00<=grade<=2.99:
        return "Fail"
    elif 3.00<=grade<=3.49:
        return 'Poor'
    elif 3.50<=grade<=4.49:
        return 'Good'
    elif 4.50<=grade<=5.49:
        return 'Very Good'
    elif 5.50<=grade<=6.00:
        return 'Excellent'
print(grades(float(input())))

#zad3
def calculations(operator,a,b):
    if operator=="multiply":
        return a*b
    elif operator=="divide":
        return int(a/b)
    elif operator=="add":
        return a+b
    elif operator=="subtract":
        return a-b

print(calculations(operator=input(),a=int(input()),b=int(input())))'''
from sys import prefix

#zad4
inpu = input()
N=int(input())
full = lambda input1,n:input1*n
print(full(inpu,N))