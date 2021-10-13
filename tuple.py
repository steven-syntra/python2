fruit_list = ["apple", "banana", "cherry", "lemon"]
fruit_tuple = tuple(fruit_list)
print(type(fruit_tuple))
print(fruit_tuple)
print(fruit_tuple[1:])

if "apple" in fruit_tuple:
    print("Yes, 'apple' is in the fruits tuple")
else:
    print("No apple!")

if "strawberry" in fruit_tuple:
    print("Yes, 'strawberry' is in the fruits tuple")
else:
    print("No strawberry!")
