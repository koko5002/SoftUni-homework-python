"""name1=input()#zad1
name2=input()
deli = input()
print(name1+deli+name2)

#zad2
meters = int(input())
print(f"{meters/1000:.2f}")

#zad3
pounds = int(input())
dollars = pounds*1.31
print(f"{dollars:.3f}")

centuries = int(input())

years = centuries * 100
days = int(years * 365.2422)   # using average year length with leap years
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

#zad5
n=int(input())
for num in range(1,n+1):
    sum_digits = 0
    digits = num
    while digits>0:
        sum_digits+=digits%10
        digits=int(digits/10)
    if(sum_digits==5) or (sum_digits==7) or (sum_digits==11):
            print(f"{num} -> True")
    else:
            print(f"{num} -> False")"""

year = int(input())
year += 1

while True:
    s = str(year)
    unique = True

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                unique = False
                break
        if not unique:
            break

    if unique:
        print(year)
        break
    year += 1


