#zad5
from itertools import count
"""
n=int(input())#number of rooms
needMore = False
chairsLeft = 0
for i in range(n):
    chairs = input().split(" ")
    freeChair = int(chairs[0].count("X"))
    visitors = int(chairs[1])

    if freeChair>=visitors:
        chairsLeft+= freeChair-visitors
    else:
        print(f"{visitors-freeChair} more chairs needed in room {i+1}")
        needMore=True

if not needMore:
    print(f"Game On, {chairsLeft} free chairs left")
    

#zad6
n=int(input())#number of electrons
filledShells = []
j=n
for i in range(1,j):
    shell = 2*i*i
    if n <= 0:
        break

    if shell<=n:
        filledShells.append(shell)
        n -= shell
    else:
        filledShells.append(n)
        break
print(filledShells)   

#zad7
sequence = list(map(int,input().split(", ")))
maxValue = 10

while sequence:
    # Step 1: Build a new list with only the numbers <= boundary
    group = [num for num in sequence if num<=maxValue]
    print(f"Group of {maxValue}'s: {group}")
    new_numbers = []## Step 2: Rebuild 'numbers' to contain only the elements > boundary
    for num in sequence:
        if num > maxValue:
            new_numbers.append(num)
    numbers = new_numbers  # overwrite old list with filtered one
"""

message = input().split(" ")

for word in message:
    num_str = ""
    letters = ""

    # separate digits and letters
    for ch in word:
        if ch.isdigit():
            num_str += ch
        else:
            letters += ch

    # swap first and last letters if needed
    if len(letters) > 1:
        letters = letters[-1] + letters[1:-1] + letters[0]

    # print decoded word
    print(chr(int(num_str)) + letters, end=" ")
