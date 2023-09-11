rain_sun = True
wind = False
fog = False

if rain_sun == False and wind == False and fog == False:
    print("Je dobre pocasi a neni treba destnik!")
elif (fog == True or rain_sun == True) and wind == False:
    print("Doporucuji vzit si destnik!")
elif wind == True and rain_sun == False:
    print("Doporucuji vzit si cepici!")
elif wind == True and rain_sun == False and fog == True:
    print("Doporucuji vzit si reflexni obleceni")
elif rain_sun == True and wind == False and fog == False:
    print("Doporucuji nevychazet!")
elif rain_sun == False and wind == False and fog == True:
    print("Doporucuji jit ven dokud je hezky!")
