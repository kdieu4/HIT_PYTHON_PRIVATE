def printUppercase(s):
    print("Uppercase chars in s are: ")
    for ch in s:
        if ch.isupper():
            print(ch, end = " ")

def printLowercase(s):
    print("\nLowercase chars in s are: ")
    for ch in s:
        if ch.islower():
            print(ch, end = " ")

print("Chao mung den CLB Tin Hoc HIT")
print('CLB Tin Hoc HIT truc thuoc Truong CNTT  - "10 diem"')

s = "CLB Tin Hoc HIT truc thuoc Truong CNTT"
printUppercase(s)
printLowercase(s)

if "CNTT" in s:
    print("\nYes")
else:
    print("\nNo")
    
print(s.swapcase())
