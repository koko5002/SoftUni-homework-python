"""def smallest(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and c>b:
        return b
    else:
        return c
print(smallest(a=int(input()), b=int(input()), c=int(input())))

def add_and_subtract(a,b,c):
    def sum_numbers():
        return a+b
    def subract(total):
       return total-c
    total=sum_numbers()#извикваме фунцкцията, да направи събирането
    return subract(total)#връщаме общия резултат чрез другата функция
a=int(input())
b=int(input())
c=int(input())
print(add_and_subtract(a,b,c))

#zad3
char1 = input()
char2 = input()
def print_symbols(char11,char22):
    for x in range(ord(char11)+1,ord(char22)):#обръщаш ги в числа та да има range
        print(chr(x),end=" ")#принтираш като го обръщаш обратно в символ
print_symbols(char1,char2)


#zad4
num = input()
def odd_even(number):
    even=0
    odd=0
    for d in number:
        n=int(d)
        if n%2==0:
            even+=n
        else:
            odd+=n
    print(f"Odd sum = {odd}, Even sum = {even}")
odd_even(num)

#zad5
list1 = input().split(" ")
def even(list2):
    evenNums = []
    for i in list2:
        n=int(i)
        if n%2==0:
            evenNums.append(n)
    return evenNums
print(even(list1))#solution without filter()

def is_even(x):
    return x%2==0
list3 = input().split(" ")
list3=[int(x) for x in list3]
even=list(filter(is_even,list3))
print(even)"""
