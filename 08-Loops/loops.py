value = 1

"""
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1
 """
"""
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equal to " + str(value))
 """

names = ["Dave", "John", "James"]
""" 
for name in names:
    print(name)

for x in "Hello":
    print(x)
 """

""" 
for x in names:
    if x == "John":
        break
    print(x)
 """

"""
for x in names:
    if x == "Dave":
        continue
    print(x)
"""

for x in range(4):
    print(x)

for x in range(2, 4):
    print(x)

for x in range(0, 100, 5):
    print(x)
else:
    print("Glad that\n's over!")

names = ['Dave', 'John', 'James']
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")