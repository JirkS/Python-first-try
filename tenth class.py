height = float(input("Zadej svoji vysku(cm): "))
weight = float(input("Zadej svoji vahu(kg): "))

BMI = weight / ((height / 100) ** 2)

if BMI < 18.5:
    print("podvaha")
elif BMI < 25:
    print("normalni vaha")
elif BMI < 30:
    print("nadvaha")
elif BMI < 40:
    print("obezita")
else:
    print("morbidni obezita")
