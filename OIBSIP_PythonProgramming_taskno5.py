import random
import string
import time

BOLD = '\033[1m'
RESET = '\033[0m'

time.sleep(1)
close=False

for letter in f"{BOLD}             >>>>>> PASSWORD GENERATOR >>>>>>>{RESET}":
    print(letter, end='', flush=True)
    time.sleep(0.02)
print("\n")
time.sleep(1)

for letter in ">Let's Generate a Password For You...\n":
    print(letter, end='', flush=True)
    time.sleep(0.02)
time.sleep(1)

while close==False:
    passlen = int(input("\n>Enter Length Of Password To Be Generated: "))
    password = []
    lowercases = list(string.ascii_lowercase)
    uppercases = list(string.ascii_uppercase)
    numbers = (1,2,3,4,5,6,7,8,9,0)
    symbols = ("!","@","#","$","%","&","_")

    for i in range(passlen):
     
         x = random.randint(1,4) # 1=>lowercase, 2=>uppercase, 3=>numbers, 4=>symbols
         if (x==1):
             add = random.choice(lowercases)
             password.append(add)
         if (x==2):
             add = random.choice(uppercases)
             password.append(add)
         if (x==3):
             add = random.choice(numbers)
             password.append(str(add))
         if (x==4):
             add = random.choice(symbols)
             password.append(add)

    final_pass = "".join(password)
    for letter in "Generated Password => ":
        print(letter, end='', flush=True)
        time.sleep(0.02)
    print(final_pass)
    print("\n")
    que = input(">Do you want to generate again? ( enter y for yes n for no ): ")
    if "y" in que:
        print("\n>Ok let's generate another password...")
        close=False

    if "n" in que:
        x = input("\n>Press Any Key To Exit.....")
        break
    exit
