# ex 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# ex 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# ex 3
for x in range(6):
    print(x)

# ex 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


# exam 1
for x in range(2, 30, 2):
    print(x, end = " ")

# exam 2
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)