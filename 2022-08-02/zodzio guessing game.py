import random

name = input("Koks tavo vardas? : ")
print("Sekmes " + name + "!")

chos = ("agurkas", "masina", "telefonas", "kompas")
chosy = random.choice(chos)

print("Bandyk atspeti raides!")

guesses = " "

turns = 5
while turns > 0:
    failed = 0
    for char in chosy:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            print(char, end=" ")
            failed += 1
    if failed == 0:
        print ("Tu laimejai!")
        print ("Zodis yra = " + chosy)
        break
    print()
    guess = input("Raide = ")
    guesses += guess
    if guess not in chosy:
        turns -= 1
        print("Neteisinga")
        print("Tu turi", + turns, " sansu atspeti")
        if turns == 0:
            print ("Tu pralaimejai!")