# The program will will ask the user for
# the base number and the power they want to raise it to
# this will then be put into a function which will get the result


def power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num
    return result


x = input("What is your base?\n")
y = input("What is the power your going too\n")
x = int(x)
y = int(y)
print(power(x, y))
