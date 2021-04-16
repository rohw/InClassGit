import string
import random


def gen_password(length):
    for i in range(length):
        print(random.randint(32, 126), end="")
