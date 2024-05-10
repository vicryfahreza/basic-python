def calculate_total(exp):
    total = 0
    for i in range(len(exp)):
        total += exp[i]
    return total

def sum(a,b=0):
    total = a+b
    print("Total: ", total)
    return total

sum(10)
john_exp = [2100, 200, 400]
windah_exp = [200, 2500, 3100]

print(calculate_total(john_exp))
print(calculate_total(windah_exp))
