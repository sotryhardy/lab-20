# Basal Metabolic Rate Calculator

weight = int(input("Wprowadź swoją wagę: "))
height = int(input("Wprowadź swój wzrost: "))
age = int(input("Wprowadź swój wiek: "))
isMale = str(input("Jesteś mężczyzną? (y/n): "))

assert isMale == "y" or isMale == "n", 'Tylko y albo n'

if isMale == "y":
    isMale = True
elif isMale == "n":
    isMale = False    
    

if isMale:
    bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
else:
    bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

bmr = round(bmr)
print(bmr)
