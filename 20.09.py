"""a=int(input())
b=int(input())
tempo = a
print("Before:\n"
      f"a = {a}\n"
      f"b = {b}")
a=b
b=tempo
print("After:\n"
      f"a = {a}\n"
      f"b = {tempo}")
#zad2
num = int(input())
if num==0 or num==1:
    print("False")
elif num>1:
    for i in range(2,num):
        if(num%i)==0:
            print("False")
            break
    else:
        print("True")
else:
    print("False")
#zad3
key = int(input())
n=int(input())
mess=""
for i in range(n):
    ch = input()
    chNum = ord(ch)
    decrypt = chr(chNum+key)
    mess+=decrypt
print(mess)"""
#zad4
n=int(input())
opening = 0
closing = 0
for i in range(n):
    inpui = input()
    if inpui=="(" and closing==opening:
        opening +=1
    elif inpui==")" and opening>closing:
        closing+=1
if closing==opening:
    print()