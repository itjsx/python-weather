def hello_world():
    print("Hello, World!")

hello_world()

def sum(num1 = 0, num2 = 0):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum(1, 2)
print(total)

print(sum("a", 2))
print(sum())

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items(1, 2, 3)

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last = "Gray")