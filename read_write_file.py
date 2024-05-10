# Write file in python
# f=open("c:\\src-data\\funny.txt", "a")
# f.write("\nI love kotlin")
# f.close()

# f=open("c:\\src-data\\funny.txt", "r")
# f_out=open("c:\\src-data\\funny_wc.txt", "w")
# for line in f:
#     token = line.split(" ")
#     f_out.write("wordcount: " +str(len(token))+line)
#
# f.close()
# f_out.close()

# With statement
with open("c:\\src-data\\funny.txt", "r") as f:
    print(f.read())

print(f.close())