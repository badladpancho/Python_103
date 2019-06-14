# This is example of If statments
# By changine the True to False or False to True this will give us
# Different Outputs

is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("This is not a male and not tall")