def myfun():
    x = float(input("enter the number"))
    y = float(input("enter the secound number"))
    operation = input("ENTER UR operation  +,-,*,/")
    if operation == "+":
        print("RESULT", x + y)
    elif operation == "-":
        print("RESULT", x - y)
    elif operation == "*":
        print("RESULT", x * y)
    elif operation == "/":
        print("RESULT", x / y)
    else:
        print("inviled enter")
yes="yes"
while yes== "yes":
        myfun()
        yes = input("do want countinue , yes or no")
print("thank you ")




