import pyautogui
import string
import itertools

allChars = (string.ascii_letters + string.digits + string.punctuation)
passlist = './vampork.txt'

print("You are being cracked B)")

def generateStuff():
    for length in range(3, 4):
        for combination in itertools.product(allChars, repeat=length):
            guess = "".join(combination)
            guess = guess + "1997"
            with open("vampork.txt", 'a') as york:
                york.write(guess)
                york.write("\n")


    for length in range(2, 3):
        for combination in itertools.product(allChars, repeat=length):
            guess = "".join(combination)
            guess = guess + "1997"
            for length2 in range(1, 2):
                for combination2 in itertools.product(allChars, repeat=length2):
                    guess2 = guess + "".join(combination2)
                    with open("vampork.txt", 'a') as york:
                        york.write(guess2)
                        york.write("\n")
    for length in range(1, 2):
        for combination in itertools.product(allChars, repeat=length):
            guess = "".join(combination)
            guess = guess + "1997"
            for length2 in range(2, 3):
                for combination2 in itertools.product(allChars, repeat=length2):
                    guess2 = guess + "".join(combination2)
                    with open("vampork.txt", 'a') as york:
                        york.write(guess2)
                        york.write("\n")
    
    for length in range(3, 4):
        for combination in itertools.product(allChars, repeat=length):
            guess = "".join(combination)
            guess = "1997" + guess
            with open("vampork.txt", 'a') as york:
                york.write(guess)
                york.write("\n")
                print("Passwords generated, time for attackalacking")


def attackalack():
    print("ok crandle add your stuff")



    # do this command when everything is done
    raise SystemExit

generateStuff()
