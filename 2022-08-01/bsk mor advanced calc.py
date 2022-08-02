
while True:
    
    action = input("Irasykite koki veiksma noresite atlikti= '+', '-', '/', '*' :")
    first = int(input("Irasykite pirmaji skaiciu = "))
    second = int(input("Irasykite antraji skaiciu = "))
    
    
    if action in ("+", "-", "*", "/"):
        if action == "+":
            print("Skaiciu suma= " + str(first + second)) 
        elif action == "-":
            print("Skaiciu atimtis= " + str(first - second))
        elif action == "*":
            print("Skaiciu daugyba = " + str(first * second))
        elif action == "/":
            print("Skaiciu dalyba = " + str(first / second))
            
    next_calc = input("Ar norite dar karta skaicuoti?(y/n) = ")
    if next_calc == "n":
        break