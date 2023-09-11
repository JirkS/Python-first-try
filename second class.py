import math

final = 14513
semi_result = (final / 92) * 100
full_result = (semi_result / 80) * 100
packages = math.ceil(full_result / 100)
print("Je potreba " +str(packages)+ " baleni semen")
