start = 1
final = 11
line = ""
for i in range(start, final):
    for x in range(start, final):
        line += str(i * x)+ " "
    print(line)
    line = ""

