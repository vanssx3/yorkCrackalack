import pyautogui
import string
import itertools

passlist = './vampork.txt'
symbols = '!?'
print("You are being cracked B)")

def generateStuff():
    for length in range(2, 3):
        for combination in itertools.product(string.ascii_letters, repeat=length):
            guess = "".join(combination)
            for length2 in range(1, 2):
                for combination2 in itertools.product(symbols):
                    guess2 = guess + "".join(combination2)
                    finalGuess = guess2 + "1997"
                    with open("vampork.txt", "a") as york:
                        york.write(finalGuess)
                        york.write("\n")


    
    print("Passwords generated, time for attackalacking")
    attackalack()

def attackalack():
    print("do the thing crandall!")



    # run this when youre done
    raise SystemExit


generateStuff()


