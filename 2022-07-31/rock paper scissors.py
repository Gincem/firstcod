import random


while True:
    user = input("Irasykite pasirinkima (Rock, paper, scissors): ")
    galimi_pasirinkimai = ["rock", "paper", "scissors"]
    kompas = random.choice(galimi_pasirinkimai)
    print(f"\nTu pasirinkai {user}, kompiuteris pasirinko {kompas}.\n")


# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.

    if user == kompas:
        print(f"abu zaidejai pasirinko {user}. Lygiosios!")
    elif user == "rock":
        if kompas == "scissors":
            print("Rock nugali scissors. Tu laimejai!")
        else:
            print("Paper nugali rock! Tu pralaimejai")
    elif user == "paper":
        if kompas == "rock":
            print("Paper nugali rock! Tu laimejai")
        else:
            print("Scissors nugali Paper! Tu pralaimejai")
    elif user == "scissors":
        if kompas == "paper":
            print("Scissors nugali Paper! Tu laimejai")
        else:
            print("Rock nugali scissors! Tu pralaimejai")        
    zaisti_dar = input("ar norite zaisti dar karta  (y/n) : ")
    if zaisti_dar.lower() != "y":
        break
        