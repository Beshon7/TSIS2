# ex 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# ex 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# ex 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# ex 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

# ex 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# ex 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# ex 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5:])

# ex 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))



# exam 1
thislist = ["apple", "banana", "cherry"]
print(thislist)

# exam 2
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# exam 3
list1 = ["apple", "banana", "cherry"] 
list2 = [1, 5, 11, 12]
list3 = [True, False, None]

# exam 4
list_1 = ["abc", 34, True, "kkk"]

# exam 5
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# exam 6
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# exam 7
thislist = ["apple", "banana", "cherry"]
for x in range(len(thislist)):
    print(thislist[x])

# exam 8
thislist = ["orange", "apple", "banana"]
thislist.sort()

# exam 9
thislist = [1, 90, 12, 11]
thislist.sort(reverse = True)
print(thislist)

# exam 10
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)

# exam 11
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)