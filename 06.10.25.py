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
print(even)

#zad6
list1=input().split(" ")
list1=[int(x) for x in list1]

print(sorted(list1))

#zad7
nums=input().split(" ")
nums=[int(x) for x in nums]
print(f"The minimum number is {min(nums)}")
print(f"The maximum number is {max(nums)}")
print(f"The sum number is: {sum(nums)}")

#zad8
nums=input().split(", ")
nums=[int(x) for x in nums]
for i in nums:
    reversed_num = int(str(i)[::-1])#string slicing
    if i==reversed_num:
        print("True")
    else:
        print("False")

def is_valid(string):
    invalid1=False
    invalid2 = False
    invalid3 = False
    if 6>len(string) or len(string)>10:#checking length of string
        print("Password must be between 6 and 10 characters")
        invalid1=True

    if not string.isalnum():#checking if string consists of only nums and letters
        print("Password must consist only of letters and digits")
        invalid2=True
    digits_count = len(list(filter(str.isdigit,string)))#algorith for finding digits in string, easy
    if digits_count<2:
        print("Password must have at least 2 digits")
        invalid3=True
    if not(invalid1 or invalid3 or invalid2):
        print("Password is valid")
password = input()
is_valid(password)"""

def perfect(nums):
    total_divisors = 0
    for i in range(1,nums):
        if nums%i==0:
            total_divisors+=i
    if nums==total_divisors:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

number = int(input())
perfect(number)