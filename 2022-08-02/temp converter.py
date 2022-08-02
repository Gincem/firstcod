


slat = input("Jusu nurodyta temp yra Celsius ar Fahrenheit? (c/f)")
if slat == "c":
    ivest_temp = float(input("Nurodykite temperatura = "))
    print("Jusu temperatura Fahrenhaitais = " + str((9 * ivest_temp + (32 * 5)) /5 ))
else:
    ivest_temp = float(input("Nurodykite temperatura = "))
    print("Jusu temperatura celsijais = " + str((ivest_temp - 32) * 5 / 9))