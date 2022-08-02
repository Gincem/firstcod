import random
n = random.randint(0,22) # gauna random skaiciu
x = 5
print("galite speti 5 kartus")
guess = int(input("irasykite skaiciu nuo 0 iki 22= "))

for i in range(1, x):
    print(i, "kartas")

    if  guess < n:
        print("sugeneruotas skaicius yra didesnis")
        guess = int(input("irasykite skaiciu nuo 0 iki 22= "))
    elif guess > n:
        print("sugeneruotas skaicius yra zemesnis")
        guess = int(input("irasykite skaiciu nuo 0 iki 22= "))
    elif guess == n:
        print("Atspejote!")
        break

print("sugeneruotas skaicius buvo= ", n)

int(input("paspauskite enter kad iseiti"))