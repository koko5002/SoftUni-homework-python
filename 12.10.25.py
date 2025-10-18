first = input().split(", ")
second = input().split(", ")
result = [word for word in first if any(word in s for s in second)]
print(result)
