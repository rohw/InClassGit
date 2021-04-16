def divisor(x):
    print("The divisors are:", end=" ")
    i = 1
    while i <= x:
        if (x % i == 0):
            print(i, end=" ")
        i += 1


x = int(input("Please enter a number for its divisors: "))

divisor(x)
