# ex 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!") 

# ex 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# ex 3
fruits = {"apple", "banana", "cherry"}
more_fruits = {"orange", "mango", "grapes"}
fruits.update(more_fruits)

# ex 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# ex 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


# exam 1
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# exam 2
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# exam 3
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# exam 4
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# exam 5
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  # удаляет случайный элемент 
print(thisset)

# exam 6
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)
print(z)

# exam 7
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)