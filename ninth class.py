PIN = "29842"
num_of_try = 0
max = 3

while num_of_try < max:
    attempt = input("Zadej pin: ")
    num_of_try += 1
    if PIN == attempt:
        print("success!")
        break
