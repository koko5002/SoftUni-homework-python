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

print(calculations(operator=input(),a=int(input()),b=int(input())))

#zad4
inpu = input()
N=int(input())
full = lambda input1,n:input1*n
print(full(inpu,N))

#zad5
def price_calc(product,number):
    total_price= 0
    if product=="coffee":
        total_price=1.5*number
    elif product=="coke":
        total_price=1.4*number
    elif product=="water":
        total_price=1.0*number
    elif product=="snacks":
        total_price=2*number
    return total_price
print(f"{price_calc(product=input(), number=int(input())):.2f}")

#zad6
def area_rect(width,height):
    area = width*height
    return area
print(area_rect(width=int(input()),height=int(input())))'''

#zad7
floats = input().split(" ")
floats = [float(x) for x in floats]
def rounding(list1):
    list2=[]
    for e in list1:
        list2.append(round(e))
    return list2
print(rounding(floats))