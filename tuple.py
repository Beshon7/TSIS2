# ex 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

# ex 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# ex 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# ex 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5:])


# exam 1
thistuple = ("apple",)
print(type(thistuple))

# exam 2
tuple1 = ("abc", 11, 140, True, 3.14)
print(tuple1)

# exam 3
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# exam 4
x = ("apple", "banana", "cherry")
y = list(x)
y.insert(0, "kiwi")
x = tuple(y)
print(x)

# exam 5
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# exam 6
fruits = ("apple", "banana", "cherry", "melon", "kiwi")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# exam 7
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *topic, red) = fruits
print(green)
print(topic)
print(red)