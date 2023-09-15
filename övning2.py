#ÖVNINGAR
#Skriv ut varie tal från 1 till 20
for i in range(1,21,1):
    print("number: " + str(i))
print("-------")

#skriv ut alla jämna tal från 1 till 20
for i in range(2,21,2):
    print("number: " + str(i))
print("-------")

#skriv ut alla udda tal från 1 till 20
for i in range(1,21,2):
    print("number: " + str(i))
print("-------")

#be användaren om två tal:
print("please give two numbers.")
num1 = input("TAL1: ")
num2 = input("TAL2: ")
#större
if(num2 > num1):
    print("TAL2 är större")
#mindre
elif(num2 < num1):
    print("TAL2 är mindre")
#samma
else:
    print("De två siffrorna är samma")
print("-----------")

#Fråga användaren hur gammal den är (i antal år).
age = int(input("Hur gammal är du? "))
#År
print("Du är " + str(age) + "år gammal")
#Månader
print("Du är " + str(age*12) + " månader gammal")
#Dagar
print("Du är " + str(age*365) + " dagar gammal")
#Sekunder
print("Du är " + str(age*365*24*3600) + " sekunder gammal")
#Om personen är 30 åring
if age > 30:
    print("true, Du är över 30 år.")
else:
    print("false, Du är under 30 år.")
