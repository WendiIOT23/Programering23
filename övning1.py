#Ovning
#Be användaren om sitt Nam och skriv ut:
#det är en tex och variabler
name = input("Vad heter du? ")
print("Hej " + name)

#Be användaren om två nummer, skriv summa av talen
#kod för två värden som ger dig ett resultat.
print("please give two numbers for me to sum up.")
num1 = input("first number: ")
num2 = input("second number: ")
sum = int(num1) + int(num2)
strsum = str(sum)
print("The result of the sum is: " + strsum)

#Be användare nam och ålder
#givet ett namn och ett värde.
#att ta emot en text med dess variabel.
name = input("vad heter du: ")
age = input("hur gamal är du: ")
print("Hej " + name + ",  du är " + age + " år gammal. ")

#Räkna ut medelvärdet av tre tal.
#Be användare om en temperatur i cesius.
#Be användare om en temperatur i Fahrenhit
celsius = int(input("age en temperatur i celsius: "))
if celsius > 20:
    print("Varm och gott ute idag")
elif celsius < 0:
    print("Kalt som gatan ute")
elif celsius > 10:
    print("ta av dig tjocktröjan nu, det är T-shirtväder")
else:
    print("en svensk normal sommar.")
#celsius.isnumric():
#farenheit = int(celsius) * 9/5 + 32
#print("temperaturen i farenheit är " + str(farenheit))
#else:
 #   print("tyvärr angav de något som inte är ett nummer")
    
print("outside of it statement")

#Be användaren om ett antal matskedar. Räkna om till teskedar.
#kod för en multiplikation.
spoon = int(input("Age ett antal matskedar: "))
mult = int(spoon) * int(3)
strmult = str(mult)
print("Du har " + strmult  + " antal teskedar.")


