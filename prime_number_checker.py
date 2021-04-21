# Prime numbers are numbers that can only be cleanly divided by itself and 1.
# https://en.wikipedia.org/wiki/Prime_number
#
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H
# Here are the numbers up to 100, prime numbers are highlighted in yellow:
# https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw


def prime_ckecker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number}:  PRIME.")
    else:
        print(f"{number}: NOT_PRIME.")


for n in range(0, 100):
    prime_ckecker(number=n)
