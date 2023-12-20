import pyautogui
import string
import itertools

allChars = (string.ascii_letters + string.digits + string.punctuation)

print("You are being cracked B)")

for length in range(4):
    for combination in itertools.product(allChars, repeat=length):
        guess = "".join(combination)
        guess = guess + "1997"
        print(guess)

for length in range(3):
    for combination in itertools.product(allChars, repeat=length):
        guess = "".join(combination)
        guess = guess + "1997"
        for length2 in range(2):
            for combination2 in itertools.product(allChars, repeat=length2):
                guess2 = guess + "".join(combination2)
                print(guess2)

for length in range(2):
    for combination in itertools.product(allChars, repeat=length):
        guess = "".join(combination)
        guess = guess + "1997"
        for length2 in range(3):
            for combination2 in itertools.product(allChars, repeat=length2):
                guess2 = guess + "".join(combination2)
                print(guess2)

for length in range(4):
    for combination in itertools.product(allChars, repeat=length):
        guess = "1997" + "".join(combination)
        print(guess)

