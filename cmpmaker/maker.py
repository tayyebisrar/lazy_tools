from datetime import datetime

now = datetime.now()

inps = input("Enter inputs and output in single string: ")
inputs = []
i_s = ""
output = inps[-1]
for inp in inps[:-1]:
    inputs.append(inp)

for x in range(len(inputs)):
    if x == 0:
        i_s = i_s + f"|  {inputs[x]}  |"
    else:
        i_s = i_s + f"  {inputs[x]}  |"

print(i_s)
table = []
n = len(inps)
a = ''
while True:
    a = input(f"{inps}: ")
    if a == "q":
        break
    if len(a) != n:
        continue
    s = ""
    for i in range(len(a)):
        if i == 0:
            s = s + f"|  {a[i]}  |"
        else:
            s = s + f"  {a[i]}  |"
        """if i != n-1:
            s = s + f"|  {a[i]}  "
        else:
            s = s + f"  {a[i]}  |"""
    print(s)
    table.append(s)
        

yn = input("Save table? (y/n)").lower()

if yn == "y":
    crrtime = now.strftime("%Y%M%D%H%M%S")
    with open(crrtime+".cmp", "w") as cmpfile:
        cmpfile.writelines(inputs)
        for line in table:
            cmpfile.writelines(line)
else:
    print("Table not saved")