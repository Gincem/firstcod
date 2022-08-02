import time

def countdown(t):
    while t >0:
        print(t)
        t -= 1
        time.sleep(1)
    print("Slat")
print("Kiek sekundziu turi eiti timeris?(Sveikas skaicius) = ")
seconds = input()
while not seconds.isdigit():
    print("Tai nera sveikas skaicius! Iveskite sveikaji skaiciu = ")
    seconds = input()
seconds = int(seconds)
countdown(seconds)