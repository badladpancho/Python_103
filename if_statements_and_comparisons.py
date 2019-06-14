#        This fuction will take 3 paramites
#       will give us the biggest number
#       Here are some of the comparison
#       == equals
#       <= less then equal to
#       >= greater then equal to
#       != not equal to
def big_number(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        print("Number 1 is the biggest");
        return print(num1);
    if num2 >= num1 and num2 >= num3:
        print("Number 2 is the biggest");
        return print(num2);
    if num3 >= num1 and num3 >= num2:
        print("Number 3 is the biggest")
        return print(num3);
first = int (input("What is the first number\n"));
sec = int(input("What is the second number\n"));
third = int(input ("What is the third number\n"));
big_number(first,sec,third);   #This is calling the fuction
