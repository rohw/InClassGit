def calc_function(x, y):
    sum = x+y
    print("Sum is ", sum)

    subt = x-y
    print("Subtraction is ", subt)

    mult = x*y
    print("Multiplication is ", mult)

    div = x/y
    print("Division is ", div)


x = int(input("Please enter a number for 'x': "))
y = int(input("Please enter a number for 'y': "))

calc_function(x, y)
