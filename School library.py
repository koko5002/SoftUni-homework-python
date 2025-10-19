shelfWithBooks = input().split("&")
command=""
while command!="Done":
    command=input()
    if command=="Done":
        break
    command=command.split(" | ")
    if (command[0]=="Add Book") and (command[1] not in shelfWithBooks):
        shelfWithBooks.insert(0,command[1])
    elif (command[0]=="Take Book") and (command[1] in shelfWithBooks):
        shelfWithBooks.remove(command[1])
    elif command[0]=="Swap Books":
        if (command[1] in shelfWithBooks) and (command[2] in shelfWithBooks):
            i=shelfWithBooks.index(command[1])
            j = shelfWithBooks.index(command[2])
            shelfWithBooks[i], shelfWithBooks[j] = shelfWithBooks[j], shelfWithBooks[i]
    elif (command[0]=="Insert Book") and (command[1] not in shelfWithBooks):
        shelfWithBooks.append(command[1])
    elif (command[0]=="Check Book") and (0<=int(command[1])<len(shelfWithBooks)):
        print(shelfWithBooks[int(command[1])])

print(", ".join(x for x in shelfWithBooks))

