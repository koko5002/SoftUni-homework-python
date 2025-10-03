"""#zad1
stri = input().split(", ")
int_list = [int(x) for x in stri]
for i in range(len(int_list)):
    if int_list[i]==0:
        int_list.pop(i)
        int_list.append(0)
print(int_list)

#zad2
list1 = input().split(" ")
ch = list(input())
message = []
for i in list1:
    digit_sum = sum(int(digit) for digit in i)
    index = digit_sum%len(ch)
    message.append(ch.pop(index))
for x in message:
    print(x,end="")

#zad3
list1 = input().split(" ")
nums = list(float(x) for x in list1)
middle = len(nums)//2
left = nums[:middle]
right = nums[middle+1:]
right.reverse()
L=0.0
R = 0.0
for i in left:
    if i==0:
        L*=0.8
    L+=i
for k in right:
    if k==0:
        R*=0.8
    R+=k

if L<R:
    print(f"The winner is left with total time: {L:.1f}")
else:
    print(f"The winner is right with total time: {R:.1f}")

#zad4
inp = input()
alive = inp.split(" ")
k=int(input())
dead=[]
index=0
while len(alive)>0:
    index=(index+k-1)%len(alive)
    dead.append(int(alive.pop(index)))
print("["+",".join(str(x) for x in dead)+"]")"""

#zad5
line1 = input().split(" ")
line2 = input().split(" ")
line3 = input().split(" ")
board = [line1,
         line2,
         line3]
winner=''
for i in range(3):
    if board[i][0]==board[i][1]==board[i][2]!='0':
        winner=board[i][0]
for c in range(3):
    if board[0][c] == board[1][c] == board[2][c] != '0':
        winner = board[0][c]
if board[0][0] == board[1][1] == board[2][2] != 0:
    winner = board[0][0]
if board[0][2] == board[1][1] == board[2][0] != 0:
    winner = board[0][2]
if winner=='1':
    print("First player won")
elif winner=='2':
    print("Second player won")
else:
    print("Draw!")
   #zad6
arr = list(map(int, input().split()))

while True:
    cmd = input()
    if cmd == "end":
        break

    parts = cmd.split()

    if parts[0] == "exchange":
        idx = int(parts[1])
        if idx < 0 or idx >= len(arr):
            print("Invalid index")
        else:
            arr = arr[idx+1:] + arr[:idx+1]

    elif parts[0] == "max":
        target = [x for x in arr if x % 2 == 0] if parts[1] == "even" else [x for x in arr if x % 2 != 0]
        if not target:
            print("No matches")
        else:
            val = max(target)
            for i in range(len(arr)-1, -1, -1):
                if arr[i] == val:
                    print(i)
                    break

    elif parts[0] == "min":
        target = [x for x in arr if x % 2 == 0] if parts[1] == "even" else [x for x in arr if x % 2 != 0]
        if not target:
            print("No matches")
        else:
            val = min(target)
            for i in range(len(arr)-1, -1, -1):
                if arr[i] == val:
                    print(i)
                    break

    elif parts[0] == "first":
        count = int(parts[1])
        if count > len(arr):
            print("Invalid count")
        else:
            target = [x for x in arr if x % 2 == 0] if parts[2] == "even" else [x for x in arr if x % 2 != 0]
            print(target[:count])

    elif parts[0] == "last":
        count = int(parts[1])
        if count > len(arr):
            print("Invalid count")
        else:
            target = [x for x in arr if x % 2 == 0] if parts[2] == "even" else [x for x in arr if x % 2 != 0]
            print(target[-count:])

print(arr)
