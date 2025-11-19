'''nums = [1, 2, 3, 4, 5, 6]
filtered = [True if x % 2 == 0 else False for x in nums ]
print(filtered)

#zad2
v = list(map(int, input().split(".")))
num = v[0]*100 + v[1]*10 + v[2] + 1
a, b, c = num // 100, (num // 10) % 10, num % 10
print(f"{a}.{b}.{c}")#обединяваме в едно число и после отделяме на цифри

#zad3
text = input().split(" ")
even = [print(word) for word in text if len(word)%2==0 ]
'''

#zad4
numbers=list(map(int,input().split(", ")))
positive = [x for x in numbers if x >= 0]
negative = [x for x in numbers if x < 0]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
#ako iskash s list comprehension, trqbva 4 times
print(f"Positive: {', '.join(map(str,positive))}")
print(f"Negative: {', '.join(map(str,negative))}")
print(f"Even: {', '.join(map(str,even))}")
print(f"Odd: {', '.join(map(str,odd))}")