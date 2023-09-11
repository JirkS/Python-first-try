exponent = int(input("Zadej kladneho a nenuloveho mocnitele: "))
if exponent <= 0:
    print("Spatne zadana hodnota!")
else:
    number = int(input("Zadej zaklad mocniny: "))
    final = number
    for i in range(exponent-1):
        final *= number
    print(str(number)+ "^" +str(exponent)+ " = " +str(final))
