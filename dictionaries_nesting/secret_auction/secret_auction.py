import os

from art import logo


def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


def str_to_int(string_param):
    result = ''.join([n for n in string_param if n.isdigit()])
    if result == '':
        return 0
    else:
        return int(result)


print(logo)
print("Welcome to the secret auction program")

bidders_dict = {

}

go_next = True
while go_next:
    name = str(input("What is your name?  \n"))
    bid = str_to_int(str(input("What is your bid?  \n")))
    bidders_dict[name] = bid
    are_there_other_bidders = str(input("Arte there any other bidders? Type 'yes' or 'no'.  \n")).lower()
    if are_there_other_bidders == 'no':
        go_next = False
    elif are_there_other_bidders == 'yes':
        clear()

max_value = 0
winner = ""
for key in bidders_dict:
    if bidders_dict[key] > max_value:
        max_value = bidders_dict[key]
        winner = key

print(f"winner is: {winner}")
