x=input("input x number: ")
y=input("input y number: ")

try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print("Exception Occurred:", e)
    z=None
except TypeError as e:
    print("Exception Occurred:", e)
    z=None

print("Division: ", z)
