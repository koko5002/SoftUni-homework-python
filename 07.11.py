#stock
from statistics import quantiles

elements=input().split(" ")
stock = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    stock[key] = int(value)
searched_products = input().split(" ")
for product in searched_products:
 if product in stock:
    print(f"We have {stock[product]} of {product} left")
 else:
    print(f"Sorry, we don't have {product}")

#statistics
products = {}
command = input()
while command!="statistics":
    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])
    if product not in products:
        products[product]=0
    products[product]+=quantity
    command=input()
totalItems = 0
print("Products in stock:")
for (key,value) in products.items():
    print(f"- {key}: {value}")
    totalItems+=value
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {totalItems}")

#ascii values
words = input().split(", ")
occurrences = {word: ord(word) for word in words}
print(occurrences)

#odd occurrences
words=input().split(" ")
dict = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in dict:
        dict[word_lower]=0
    dict[word_lower]+=1
for (key,value) in dict.items():
    if value%2!=0:
        print(key,end=" ")

#word synonyms
n = int(input())
synonyms ={}
for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word]=[]
    synonyms[word].append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")