import math

# You are painting a wall.
# The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height ✖️ wall width) ÷ coverage per can.

height = int(input("Please, input your HEIGHT: "))
width = int(input("Please, input your WIDTH: "))
coverage = int(input("Please, input your COVERAGE: "))


def calculate_number_of_cans(height, width, coverage):
    number_of_cans = int(math.ceil(height * width / coverage))
    print(f'You will need {number_of_cans} of cans to paint')


calculate_number_of_cans(height=height, width=width, coverage=coverage)
