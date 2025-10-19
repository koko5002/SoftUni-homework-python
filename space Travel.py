travelRoute= input().split("||")
fuelStart = int(input())
ammoStart = int(input())
for route in range(len(travelRoute)):
    if travelRoute[route]=="Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    temp=travelRoute[route].split(" ")
    command = temp[0]
    numberToUse=int(temp[1])
    if command=="Travel":
        if fuelStart>=numberToUse:
            fuelStart-=numberToUse
            print(f"The spaceship travelled {numberToUse} light-years.")
        else:
            print("Mission failed.")
            break
    elif command=="Enemy":
        if ammoStart>=numberToUse:
            ammoStart-=numberToUse
            print(f"An enemy with {numberToUse} armour is defeated.")
        elif fuelStart>numberToUse*2:
            fuelStart-=numberToUse*2
            print(f"An enemy with {numberToUse} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif command=="Repair":
        ammoStart+=2*numberToUse
        fuelStart+=numberToUse
        print(f"Ammunitions added: {numberToUse*2}.")
        print(f"Fuel added: {numberToUse}.")



