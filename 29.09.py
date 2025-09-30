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
    print(x,end="")"""

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