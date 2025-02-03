# ex 1
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))

# ex 2
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020

# ex 3
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"

# ex 4
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
} 
car.pop("model")

# ex 5
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()


# exam 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964,
    "year": 2020
}
# print(thisdict)

# exam 2
thisdict = dict(name = "Jonh", age = 36, country = "Norway")
print(thisdict)

# exam 3
thisdict = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}
x = thisdict.keys()
print(x)