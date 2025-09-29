"""#zad1
inp = input()
splitList = inp.split(" ")
aim= []
for i in range(len(splitList)):
    a = int(splitList[i])*(-1)
    aim.append(a)
print(aim)

#zad2
factor= int(input())
count = int(input())
list1=[]
for i in range(1,count+1):
    a=i*factor
    list1.append(a)
print(list1)

#zad3
a=11
b=11
foundNumsA = []
foundNumsB = []
cards = input()
list1=cards.split(" ")
gameOver = False
for i in range(len(list1)):
    temp = list1[i].split("-")

    if ("A" in temp[0]) and (temp[1] not in foundNumsA):
        a-=1
        foundNumsA.append(temp[1])
    elif ("B" in temp[0]) and (temp[1] not in foundNumsB):
        b-=1
        foundNumsB.append(temp[1])
    else:
        continue
    if a < 7 or b < 7:
        gameOver=True
        break
print(f"Team A - {a}; Team B - {b}")
if gameOver:
    print("Game was terminated")

#zad4
numbers = list(map(int, input().split(", ")))
beggars_count = int(input())

result = []

for beggar_index in range(beggars_count):
    total = 0
    for i in range(beggar_index, len(numbers), beggars_count):
        total += numbers[i]
    result.append(total)

print(result)

#zad5
inp = input()
list1 = [int(x) for x in inp.split(" ")]
n=int(input())
# copy and sort to find the n smallest
temp = list1.copy()
temp.sort()
# remove the n smallest
smallest_to_remove = temp[:n]
# build result: keep only elements not in smallest_to_remove
result = list1.copy()
for num in smallest_to_remove:
    result.remove(num)  # removes only one occurrence each

# print
print(", ".join(str(x) for x in result))"""

#zad7
presents = input()
list1=presents.split(" ")
i=""
while i!="No Money":
    i=input()
    temp=i.split(" ")
    if "OutOfStock" in temp[0]:
        for j in range(len(list1)):
            if temp[1]==list1[j]:
                list1[j] = "None"
            else:
                continue
    elif "Required" in temp[0]:
        index = int(temp[2])
        if 0 <= index < len(list1):
            list1[index]=temp[1]
    elif "JustInCase" in temp[0]:
        list1[-1]=temp[1]
    if i=="No Money":
        break
for k in list1:
    if k!="None":
        print(k, end=" ")


