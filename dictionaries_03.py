
"""
Python Dictionary:
are used to store data values in Key:value pairs
syntax: written with curly brackets, and have keys and values:
this Dict is a collection which is ordered, changeable and does not allow duplicates

"""

myCar = {
    "brand": "Benz",
    "model": "GLK",
    "year": 2030,
    "email": "example@gmail.com",
    "color": ["red", "white", "black"]
}
print(myCar)
# here we pick by each items
print(myCar["brand"])

#  for the length:
print(len(myCar))

#  for type: which returns the class
print(type(myCar))

#  using get() will return the same result
c = myCar["model"]
print(c)
d = myCar.get("year")
print(d)

# the key() this returns a list of all the keys in the dictionary
f = myCar.keys()
print(f)

# here we added more value to the dict
myCar["price"] = 2000
print(f)

# getting values
g = myCar.values()
print(g)

# updating a dict
myCar["year"] = 2023
print(g)

# trying to update the color which has an arrays of color
myCar["color"] = "black"
print(g)

# item() this returns eachitem in a dict as tuples in a list
h = myCar.items()
print(h)

# checking if Keys Exists with < in >keyword

if "brand" in myCar:
    print("Yes, 'brand' is one of the keys in the myCar dict")

#  updating both Keys and values we use update() method
myCar.update({"year": 2050})
print(myCar)

# removing both with pop()
myCar.pop("price")
print(myCar)

# popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
myCar.popitem()

#  we can also use < del > keyword to remove item with specified key name:
del myCar["year"]
print(myCar)

# NB: del can also delete the dictionary completely
# del myCar
# if you del the dict and still wants to print myCar it gives error b'cos myCar is no longer exists

# While clear() method empties the dictionary
# myCar.clear()


# Looping through a dictionary by using a < for > loop
# NB: when looping, the return value are the keys but some method can return the values as well
print("========================Loops========================")
# getting the keys
for car in myCar:
    print(car)

#  getting the values
for cars in myCar:
    print(myCar[cars])

#  we can also use value() method to return
for Car in myCar.values():
    print(Car)

#  same as using Keys() to return the keys dict
for CAR in myCar.keys():
    print(CAR)

# here we use item() method to get both keys and values
for caR, cAr in myCar.items():
    print(caR, cAr)

# Dictionaries coping
keke = myCar.copy()
print(keke)

# another way of coping a dict is with dict() keyword
bus = dict(keke)
print(bus)
print(myCar)
print(keke)

print("=====================Nested Dict============================")

# Nested Dict: this is where a dict can contain another dictionaries, it's called nested dictionary
myStudents ={
    "java": {
        "name": "Johnson",
        "year": 2020
    },
    "web":{
        "name": "cakahal",
        "year": 1999
    },
    "python":{
        "name": "Uba",
        "year": 2023
    }
}

print(myStudents)

# another way of creating dictionaries that will contain other dict
python1 = {
    "name": "johnson",
    "age": 70
}
python2 = {
    "name": "cakahal",
    "age": 10
}
python3 = {
    "name": "Uba",
    "age": 50
}

myPython = {
    "python1": python1,
    "python2": python2,
    "python3": python3
}

print(myPython)
# dict methods
# here to remove all elements from a dict list with clear() it only removes the items inside
keke.clear()
print(keke)

# fromkeys() methods returns a dict with the specified keys and the specified value
# syntax: dict.fromkeys(keys, values)
# where: keys Required, an iterable specifying the keys of the new dict
# where: value Optional. the value for all keys Default value is none

x = ('key1', 'key2', 'key3')
y = 0
# y = bus
fkey = dict.fromkeys(x,y)
print('Fromkey', fkey)

#  copy()
# get()
# update()
# item()
# pop()
# popitem()
# values()
#

# setdefault() method returns the value of the item with the specified key, if the key does not exist, insert the key,
# with the specified value...
# syntax: dictionary.setdefault(keyname, value)
# where: keyname is Required, the keyname of the item you want to return the value from
# where: value is Optional, if the key exist, this parameter has no effect, is the key does not exist,
# this value becomes the key's value...then Default value None

MyCar = {
    "brand": "Benz",
    "model": "GLK",
    "year": 2030,
    "email": "example@gmail.com",
}
c = MyCar.setdefault("color", "white")
print(c)
print(MyCar)

