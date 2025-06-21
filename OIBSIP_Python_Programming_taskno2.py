import time

for letter in ">>> Hello User!!":
    print(letter, end='', flush=True)
    time.sleep(0.02)
print("\n")
time.sleep(1)

bmidef = "Let's learn what BMI actually is! =>\nThe Body Mass Index (BMI) is a number derived from \nthe ratio of a person's weight to their height, \nused to classify individuals into different weight categories.\n\nThe Formula is:"
bmiformula = ">>>>>  BMI = weight (kg) / [height (m)]²"

for letter in bmidef:
    print(letter, end = '', flush=True)
    time.sleep(0.02)
print("\n")

for letter in bmiformula:
    print(letter, end='', flush=True)
    time.sleep(0.02)

print("\n\n")
time.sleep(1)

for letter in "Let's Calculate Your BMI !!\n":
    print(letter, end='', flush=True)
    time.sleep(0.02)

w = int(input("ENTER YOUR WEIGHT IN KG > "))
h = float(input("ENTER YOUR HEIGHT IN METER > "))

bmitemp = w/(h*h)
bmi = round(bmitemp, 2)

if bmi<18.5:
    categ = "UNDERWEIGHT"
if bmi>=18.5 and bmi<=24.9:
    categ = "HEALTHY WEIGHT"
if bmi>=25 and bmi<29.9:
    categ = "OVERWEIGHT"
if bmi>=30:
    categ = "OBESE"

result = f"\n>> According to your weight {w} and your height {h},\nYour BMI shall be: {bmi} \nwhich comes under ( {categ} ) category!!\n\nThankyou For Using This Tool... <3"

for letter in result:
    print(letter, end='', flush=True)
    time.sleep(0.01)

x = input("\n\nPress ANY KEY to exit....")
