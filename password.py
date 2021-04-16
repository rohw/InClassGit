import string
import random


def gen_password(length):
    charactor = string.ascii_letters + string.digits
    print("Generated password: ", end=")
    for i in range(length):
        print(random.choice(charactor), end="")


x = int(input("Enter number of characters that you want your password to be: "))

gen_password(x)
