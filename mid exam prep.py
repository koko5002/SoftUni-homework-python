'''#counter strike
energy = int(input())
battlesWon = 0
while True:
    enemyDistance = input()

    if enemyDistance=="End of battle":
        print(f"Won battles: {battlesWon}. Energy left: {energy}")
        break
    enemyDistance=int(enemyDistance)
    if energy<enemyDistance:
        print(f"Not enough energy! Game ends with {battlesWon} won battles and {energy} energy")
        break
    else:
        energy-=enemyDistance
        battlesWon+=1
    if battlesWon%3==0:
        energy+=battlesWon




#shoot for the win
peopleWaiting = int(input())
currentState = list(map(int,input().split(" ")))
i=0
for i in range(len(currentState)):
    possible = 4-currentState[i]
    currentState[i]+= possible
    peopleWaiting-=possible
    if peopleWaiting<possible:
        currentState[-1]=peopleWaiting
        print(f"The lift has empty spots!")
        print(" ".join(str(x) for x in currentState))
else:
    print(f"There isn't enough space! {peopleWaiting} people in a queue!")
    print(" ".join(str(x) for x in currentState))
import math




#numbers
sequence = list(map(int,input().split(" ")))
avg = sum(sequence)/len(sequence)
winners = []
#winners = [x for x in sequence if x>avg and len(winners)<=5 ]
for x in sequence:
    if x>avg:
        winners.append(x)
winners = sorted(winners, reverse=True)[:5]
if len(winners)<1:
    print("No")
else:
    print(" ".join(str(x) for x in winners))





#SOFTUNI RECEPTION
first = int(input())
second = int(input())
third = int(input())
studentCount = int(input())
hours=0
studentsPerHour = first+second+third
while studentCount>0:
    if hours%4==0:
        hours += 1
        continue
    studentCount -= studentsPerHour
    if studentCount <= 0:
        break
    hours += 1
print(f"Time needed: {hours}h.")




#TREASURE HUNT
loot = input().split("|")
temp=""

while temp!="Yohoho!":
    temp=input().split(" ")
    if temp[0]=="Loot":
        for i in range(1,len(temp)):
            if temp[i] not in loot:
                loot.insert(0,temp[i])
    elif temp[0]=="Drop":
        if 0<=int(temp[1])<=len(loot): #valid
            itemIndex = int(temp[1])#index of item
            item=loot[itemIndex]#value of the item
            loot.pop(itemIndex)#removing by index
            loot.append(item)#inserting at end
        else:
            continue
    elif temp[0]=="Steal":
        stolen=[]
        if int(temp[1])<=len(loot):
            stolen=loot[-int(temp[1]):]#steal the last count elements if enough are there
            del loot[-int(temp[1]):]# delete last 'count' elements
        else:
            stolen=loot[:]    # steal all if count is bigger
            loot.clear()  # clear entire list
        print(", ".join(stolen))
    elif temp[0]=="Yohoho!":
        break

if len(loot)==0:
    print("Failed treasure hunt.")
else:
    treasureGain = sum(len(x) for x in loot) / len(loot)
    print(f"Average treasure gain: {treasureGain:.2f} pirate credits.")'''


#MOVING TARGET
targets = list(map(int,input().split(" ")))
command = ""
while command!="End":
    command=input()

    if command=="End":#quickly end it
        break
    command= command.split(" ")
    indexToUse = int(command[1])#every command has index at this position

    if command[0]=="Shoot":
        if 0<=indexToUse<len(targets):#check if index is valid
            targets[indexToUse]-=int(command[2])
            if targets[indexToUse]<=0:#check if target is shot
                targets.pop(indexToUse)
        else:
            continue

    elif command[0]=="Add":
        if 0 <= indexToUse < len(targets):
            targets.insert(indexToUse,int(command[2]))#Insert a target with the received value at the received index if it exists.
        else:
            print("Invalid placement!")

    elif command[0]=="Strike":
        radius = int(command[2])
        if indexToUse-radius>=0 and indexToUse+radius<len(targets):
            del targets[indexToUse-radius:indexToUse+radius+1]
        else:
            print("Strike missed!")

print("|".join(str(x) for x in targets))