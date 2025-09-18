'''#zad1
int1=int(input())
int2 = int(input())
int3=int(input())
int4=int(input())
total=((int1+int2)//int3)*int4
print(total)
#zad2
s=input()
x=input()
c=input()
print(s+x+c)

#zad3
import math
people= int(input())
n=int(input())
courses = math.ceil(people/n)
print(courses)

#zad4
N = int(input())
sumo=0
for i in range(N):
    letter= input()
    sumo+=ord(letter)
print(f"The sum equals: {sumo}")

#zad5
start = int(input())
end = int(input())
for i in range(start,end+1,1):
    print(chr(i),end=" ")
#zad6
N=int(input())
for i in range(0,N):
    for j in range(0,N):
        for c in range(0,N):
            print(f"{chr(97+i)}{chr(97+j)}{chr(97+c)}")
#zad7 capacity = 255
n=int(input())
capacity = 0
for i in range(n):
    lit = int(input())
    if (capacity+lit)>255:
        print("Insufficient capacity!")
        capacity=capacity
    else:
        capacity+=lit
print(capacity)
#zad8
import math
groupSize = int(input())
days = int(input())
coins = 0
for i in range(1,days+1):

    if i%10==0:
        groupSize-=2
    if i%15==0:
        groupSize+=5
    coins += 50
    coins-= 2*groupSize#food
    if i%3==0:
        coins -= 3*groupSize#water
    if i%5==0:
        coins+=20*groupSize
        if i%3==0:
            coins-=2*groupSize

print(f"{groupSize} companions received {math.floor(coins/groupSize)} coins each.")
#zad9
N=int(input())#number of snowballs
maxValue=0
w=0
t=0
q=0
for i in range(N):
    weight=int(input())
    time = int(input())
    quality=int(input())
    value = (weight/time)**quality
    if value>maxValue:
        maxValue=value
        w=weight
        t=time
        q=quality
print(f"{w} : {t} = {maxValue:.0f} ({q})")'''

lostFights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
h=0
s=0
sh=0
ar=0
for i in range(1,lostFights+1):
    if i%2==0:
        h+=1
    if i%3==0:
        s+=1
        if i % 2 == 0:

            sh+=1
            if sh % 2 == 0:
                ar += 1

total= (h*helmet) + (s*sword) + (sh*shield) + (ar*armor)
print(f"Gladiator expenses: {total:.2f} aureus")


