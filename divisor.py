def divisor(x):
    print("The divisors are: ")
    i = 1
    while i <= x:
        if (x % i == 0):
            print(i)
        i += 1
