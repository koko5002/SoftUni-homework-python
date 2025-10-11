'''#zad1
text = input()
list1 = [x for x in text]
vowels = ['a','o','u','e','i','I','A','O','U','E']
voweless = "".join(x for x in list1 if x not in vowels)
print(voweless)

#zad2
wagons = int(input())
wagonList = [0 for x in range(wagons)]
command = ''
while command!="End":
    command=input().split(" ")
    if command[0]=="add":
        wagonList[-1]+=int(command[1])
    elif command[0]=="insert":
        wagonList[int(command[1])]+=int(command[2])
    elif command[0]=="leave":
        wagonList[int(command[1])]-=int(command[2])
    elif command[0]=="End":
        print(wagonList)
        break

#zad3
notes = [0]*10
while True:
    command = input()
    if command=='End':
        break
    tokens = command.split("-")
    priority = int(tokens[0])-1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority,note)

result = [x for x in notes if x!=0]
print(result)

#zad4
vhod = input()
words = vhod.split(" ")
palindrome = input()
found = [word for word in words if word=="".join(reversed(word))]
print(found)
print(f"Found palindrome {found.count(palindrome)} times")


#zad5
names_list = input().split(", ")
sorted_list = sorted(names_list, key=lambda x:(-len(x),x))
print(sorted_list)

#zad6
numbers_list = list(map(int,input().split(", ")))
found_indices = map(lambda x: x if numbers_list[x]%2==0 else 'no', range(len(numbers_list)))
even_indices = list(filter(lambda a:a!='no',found_indices))
print(even_indices)'''

#zad7
employees = input().split(" ")
improvement_factor = int(input())
employees = list(map(lambda x:int(x)*improvement_factor,employees))
filtered = list(filter(lambda x: x>=(sum(employees)/len(employees)),employees))
if len(filtered)>=len(employees)/2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")