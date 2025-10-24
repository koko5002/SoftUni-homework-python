''''#zad Comment
class Comment:
    def __init__(self, username,content,likes=0):
        self.username = username
        self.content = content
        self.likes= likes

#zad Party
class Party:
    def __init__(self):
        self.people = []
party=Party()
line=input()
while line!="End":
    party.people.append(line)
    line=input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")


#zad Email
class Email:
    def __init__(self,sender,receiver,content,):
        self.sender = sender
        self.receiver = receiver
        self.content= content
        self.is_sent=False

    def get_Info(self):
            return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

    def send(self):
        self.is_sent=True


emails =[]
line=input()
while line!="Stop":
    tokens = line.split(" ")
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens [2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line=input()
sendEmails = list(map(lambda x: int(x), input().split(", ")))
for x in sendEmails:
    emails[x].send()
for email in emails:
    print(email.get_Info())



class Zoo:
    __animals = 0#•	The underscores in front of the animal's attribute is used to express that it is private. It is not meant to be used outside the class.
    def __init__(self,name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []
    def add_animal(self,species,name):
        if species=="mammal":
            self.mammals.append(name)
        elif species=="fish":
            self.fishes.append(name)
        elif species=="bird":
            self.birds.append(name)
        Zoo.__animals+=1
    def get_info(self,species):
        result = ""
        if species=="mammal":
            result+=f"Mammals in {self.name_zoo}: {', '.join(self.mammals)}\n"
        elif species=="fish":
            result += f"Fishes in {self.name_zoo}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name_zoo}: {', '.join(self.birds)}\n"
        result +=f"Total animals: {Zoo.__animals}"
        return result
zoo_name=input()
zoo=Zoo(zoo_name)
count=int(input())
for i in range(count):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species,name)
info= input()
print(zoo.get_info(info))'''

class Circle:
    __pi=3.14
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius=diameter/2
    def calculate_area(self):
        return Circle.__pi*self.radius*self.radius
    def calculate_circumference(self):
        return Circle.__pi*self.diameter
    def calculate_area_of_sector(self,angle):
        return (angle/360)*Circle.__pi*self.radius*self.radius