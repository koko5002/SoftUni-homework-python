'''#zad1
def data_types(type, value):
    if type=='int':
        print(int(value)*2)
    elif type   =="real":
        print(f"{float(value)*1.5:.2f}")
    elif type=="string":
        print(f"${value}$")

data_types(type=input(),value=input())'''

#zad2
import math
def center_point():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    if (abs(x1)<=abs(x2)) and (abs(y1)<=abs(y2)):
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")

center_point()
#zad5
a = int(input())
b = int(input())
c = int(input())

if a == 0 or b == 0 or c == 0:
    print("zero")
else:
    negatives = 0
    for x in (a, b, c):
        if x < 0:
            negatives += 1
    if negatives % 2 == 0:
        print("positive")
    else:
        print("negative")
