exp=[2100, 2980, 2400, 3100, 2200]
total=0
# for item in exp:
#     total += item
# print(total)

print("===========")

for i in range(len(exp)):
    print("Month: ", (i+1), "Expense: ", exp[i])
    total += exp[i]

print("Total Expense: ", total)

key_location="chair"
location=["garage", "living room", "chair", "closet"]

for i in location:
    if i==key_location:
        print("Found The Key in: ", i)
        break
    else:
        print("Key Not found in: ", i)


ikan_laut="Clownfish"
ikan=["catfish", "Guramii", "Arapaima", "Clownfish", "Botia"]

for i in ikan:
    if i==ikan_laut:
        print("Ditemukan ikan laut dari list yaitu: ", i)
        break
    else:
        print("Bukan ikan laut: ", i)

print("===========")

for i in range(1,6):
    if i%2 == 0:
        continue
    print(i*i)


