def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

def pow(a, b):
    return a ** b

def module(a, b):
    return a % b

def compare(a, b):
    if (a > b):
        return "a is greater than b"
    elif(a < b):
        return "a is smaller than b"
    else:
        return "a is equal to b"
    
def myAnd(a, b):
    return a and b

def myOr(a, b):
    return a or b

def myXor(a, b):
    return a ^ b

def notEqual(a, b):
    return not (a == b)

def myRightShift(a):
    return a << 5

def myLeftShift(a):
    return a >> 6

def reverseBinary(a):
    print("Chuỗi nhị phân ngược lại là: ")
    while (a > 0):
        print(f"{a % 2} ")
        a //= 2

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"Sum of {a} and {b} is {add(a, b)}")
print(f"Difference of {a} and {b} is {sub(a, b)}")
print(f"Product of {a} and {b} is {mul(a, b)}")
print(f"The quotient of {a} divided by {b} is {div(a, b)}")
print(f"The exponentiation of {a} to the power of {b} gives {pow(a, b)}")
print(f"The reminder when {a} divided by {b} is {module(a, b)}")
print(compare(a, b))
print(f"{a} AND {b} = {myAnd(a, b)}")
print(f"{a} OR {b} = {myOr(a, b)}")
print(f"{a} XOR {b} = {myXor(a, b)}")
print(f"{a} dịch phải 5 bit: {myRightShift(a)}")
print(f"{a} dịch trái 6 bit: {myLeftShift(a)}")
reverseBinary(a)

