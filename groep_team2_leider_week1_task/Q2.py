
# Vraag de gebruiker om een getal in te voeren
number = int(input("enter the  positief numb : "))

print("Even getallen met een for-lus:")
for i in range(0, number + 1, 2):
    print(i)

print("\nEenter the  positief numb :")
i = 0
while i <= number:
    print(i)
    i += 2
