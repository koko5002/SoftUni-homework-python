'''
tail = input()
body = input()
head = input()
list1=[head,body,tail]
print(list1)
#zad2
n = int(input())
list1=[]
for i in range(n):
    inp = input()
    list1.append(inp)
print(list1)

#zad3
positive=[]
negative=[]
n=int(input())
for i in range(n):
    it = int(input())
    if it>=0:
        positive.append(it)
    else:
        negative.append(it)
print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")

#zad4
n=int(input())
word = input()
list1=[]
for i in range(n):
    it = input()
    list1.append(it)
print(list1)
list2=[]
for i in range(len(list1)):
    if word in list1[i]:
        list2.append(list1[i])
print(list2)'''

#zad5
n=int(input())
list1 = []
list2=[]
for i in range(n):
    inti = int(input())
    list1.append(inti)
word = input()
for a in range(len(list1)):
    if word=="even" and list1[a]%2==0:
        list2.append(list1[a])
    elif word=="odd" and list1[a]%2!=0:
        list2.append(list1[a])
    elif word=="negative" and list1[a]<0:
        list2.append(list1[a])
    elif word=="positive" and list1[a]>=0:
        list2.append(list1[a])
print(list2)