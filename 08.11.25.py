'''''#1.	Count Chars in a String
words = input()
letters = [ch for ch in words if ch!=" "]
dict = {}
for ch in letters:
    if ch not in dict:
        dict[ch]=0
    dict[ch]+=1
for key,value in dict.items():
    print(f"{key} -> {value}")

#2.	A Miner Task
dict={}
while True:
    resource=input()
    if resource=="stop":
        break
    quantity = int(input())
    if resource not in dict:
            dict[resource]=0

    dict[resource]+=quantity
for resource, quantity in dict.items():
    print(f"{resource} -> {quantity}")

#3capitals
dicti= {}
country = input().split(", ")
capitals = input().split(", ")
for co in range(len(country)):
    dicti[country[co]]=capitals[co]
for key,value in dicti.items():
    print(f"{key} -> {value}")

#4
phonebook = {}

# Read entries until you get a number (N)
while True:
    command = input()
    if command.isdigit():
        n = int(command)
        break
    name, number = command.split("-")
    phonebook[name] = number  # overwrites if name already exists

# Perform N lookups
for _ in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")

'''
#5
materials = {"shards": 0, "fragments": 0, "motes": 0}
junk={}
while True:
    inpu = input().split(" ")
    obtained = False
    for i in range(0,len(inpu),2):
        mat = inpu[i+1].lower()
        quantity=int(inpu[i])
        if mat in materials:
            materials[mat] += quantity
        else:
            if mat not in junk:
                junk[mat] = 0
            junk[mat] += quantity
        if materials["shards"]>=250:
            materials["shards"]-=250
            print("Shadowmourne obtained!")
            obtained=True
            break
        elif materials["fragments"]>=250:
            materials["fragments"] -= 250
            print("Valanyr obtained!")
            obtained=True
            break
        elif materials["motes"]>=250:
            materials["motes"] -= 250
            print("Dragonwrath obtained!")
            obtained=True
            break
    if obtained:
        break
print(f"shards: {materials['shards']}")
print(f"fragments: {materials['fragments']}")
print(f"motes: {materials['motes']}")
for key,value in junk.items():
    print(f"{key}: {value}")