# def greet():
#     print('do something')
#
#
# greet()

# def greet_with_name(name):
#     print(f'Hello {name}')
#     print(f'How do you do {name}?')
#
#
# greet_with_name(input("Please input your name: "))

def greet_with(name, location):
    print(f'Hello {name} from {location}')
    print(f'How do you do {name} from {location}?')

# ==== Positional arguments =======
greet_with("Alex", "Odessa")

# ==== Arguments with the names =======
greet_with(location="New York", name="Red")
