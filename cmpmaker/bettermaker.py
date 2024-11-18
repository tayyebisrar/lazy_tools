# This version will automatically increment the input,
# e.g. 0001 to 0010, instead of typing manually
from datetime import datetime
import random
now = datetime.now()

inps = input("Enter inputs and output in single string: ")
inputs = []
i_s = ""
for inp in inps:
    inputs.append(inp)

for x in range(len(inputs)):
    if x == 0:
        i_s = i_s + f"|  {inputs[x]}  |"
    else:
        i_s = i_s + f"  {inputs[x]}  |"

print(i_s)
table = []
n = len(inps)

for i in range(0, 2**(len(inps)-1)):
        b = bin(i)[2:].zfill(len(inps)-1)
        o = input(f"{b}: ")
        s = ''
        for j in range(len(str(b))):
            if j == 0:
                s = s + f"|  {str(b)[j]}  |"
            else:
                s = s + f"  {str(b)[j]}  |"
        s = s + f"  {o}  |"
        table.append(s)

yn = input("Save table? (y/n)").lower()

if yn == "y":
    crrtime = now.strftime("%Y%H%M%S") + str(random.randint(0, 1000000))
    with open(crrtime+".cmp", "w") as cmpfile:
        cmpfile.writelines(i_s)
        cmpfile.write("\n")
        for line in table:
            cmpfile.writelines(line)
            cmpfile.write("\n")
else:
    print("Table not saved")