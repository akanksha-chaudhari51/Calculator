print("----------CALCULATOR----------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
ch = int(input("Enter Your Choice: "))

if ch in [1, 2, 3, 4, 5]:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    
    def add(a,b):
        print("Addition of",a,"and",b,"is",a+b)

    def sub(a,b):
        print("Subtraction of",a,"and",b,"is",a-b)

    def mul(a,b):
        print("Multiplication of",a,"and",b,"is",a*b)

    def div(a,b):
        if b != 0:
            print("Division of",a,"and",b,"is",a/b)
        else:
            print("Error! Division by zero is not allowed")

    def mod(a,b):
        print("Modulus of",a,"and",b,"is",a%b)

    if ch == 1:
        add(a,b)
    elif ch == 2:
        sub(a,b)
    elif ch == 3:
        mul(a,b)
    elif ch == 4:
        div(a,b)
    elif ch == 5:
        mod(a,b)

else:
    print("Invalid Choice.")