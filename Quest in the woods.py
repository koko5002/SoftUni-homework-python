#quest in the woods
N = int(input())
participants = int(input())
groupEnergy = float(input())
waterPerDayPerPerson = float(input())
foodPerDayPerPerson = float(input())

totalFood = N*participants*foodPerDayPerPerson
totalWater = N*participants*waterPerDayPerPerson

for i in range(1,N+1):
    choppingWood = float(input())
    groupEnergy -= choppingWood
    if groupEnergy<=0:
        print(f"You will run out of energy. You will be left with {totalFood:.2f} food and {totalWater:.2f} water.")
        break
    if i%2==0:
        groupEnergy*=1.05
        totalWater*=0.7
    if i%3==0:
        groupEnergy*=1.1
        totalFood-= totalFood/participants
else:
    print(f"You are ready for the quest. You will be left with {groupEnergy:.2f} energy!")