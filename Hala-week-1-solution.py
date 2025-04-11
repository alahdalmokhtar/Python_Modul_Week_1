# Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.

for number in range(1,11):
    print(number)

#Question 2: Take a number input from the user and write a Python program that
# prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops.

user_number = int(input("please enter a number:"))
for even_number in range(1, user_number+1):
    if even_number%2 == 0:
     print(f"even numbers untill {user_number} are : {even_number}")

even_number_1 = 1
while even_number_1 <= user_number:
  if even_number_1 %2 == 0:
    print(f"even numbers untill {user_number} are : {even_number_1}")
  even_number_1 += even_number_1

#Question 3: Write a Python code that receives a start and end value from the user and
#  prints all the numbers between these values ​​(including the end value) on the screen.

start_number = int(input("inter a start number: "))
end_number = int (input("inter end number: "))

for numbers in range(start_number , end_number+1):
   print (numbers)

#Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.

user_number = int(input("inter a number: "))
if user_number %2 ==0:
    print(f"the number that you entered {user_number} is even")
else:
    print(f"the number that you entered {user_number} is odd")


#Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial. 
# Factorial is the product of all positive integers between a number itself and 1. 
# For example: if the user entered 5, the program should give the following output: 
# Enter a number from the user: 5 Factorial: 120

user_number= int(input("inter a positive number: "))
if user_number < 1:
    print("number is not positive")
else:
    factorial = 1
    number = user_number

    while number > 1:
        factorial *= number
        number -= 1
       

    print(f"Factorial: {factorial}")

#Question 6: Write a Python code that receives a number from the user and checks whether this number is prime.

number = int(input("inter a number: "))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not prime")
            break
    else:
        print(f"{number} is prime")

#Question 7: How to create a loop that calculates the Fibonacci sequence and 
# returns the result as a list containing numbers up to a certain limit?

number = int(input("inter a number: "))
fibonacci = [0, 1]
for i in range(2, number):
    next_number = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_number)   

print(fibonacci)



#Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.
wrod_user = input("inter a word: ")
reverse_word =wrod_user[::-1]
print(reverse_word)

#Question 9: How to create a combination of loop and conditional statement that takes 
# a word input from the user and checks whether that word is a palindrome (the same when read backwards)?

user_word = input("inter a word: ")
if user_word == user_word[::-1]:
    print(f"{user_word} is palindrome")
else:
    print(f"{user_word} is not palindrome")

#Question 10: Write the code that calculates the person's weight index and returns the result as underweight, 
# overweight or overweight according to the index value. (You can look on the internet for the weight index calculation)
#  To do this, ask the user for their weight and height measurements. weight index If it is below 25, it is weak,
#  Between 25-30 is normal, If you are over 30-40, you are overweight. If you are over 40, you are overweight.

weight = float(input("inter your weight in kg: "))
height = float(input("inter your height in cm: "))
weight_index =  weight/((height/100)**2)
if weight_index < 25:
    print(f"your weight index is {weight_index} :underweight")
elif weight_index >= 25 and weight_index <= 30:
    print(f"your weight index is {weight_index}: normal")
elif weight_index>= 30 and weight_index<=40 :
    print (f"your weight index is {weight_index}: overweight")
elif weight_index > 40:
    print(f"your weight index is {weight_index}: obese")


#Question 11: How to write a Python program that finds the largest of three numbers entered by a user?
numbers =[]
for i in range(1,4):
    number = int(input("inter a number:"))
    numbers.append(number)
largest_number = max(numbers)
print(f"the largest number is {largest_number}")


#Question 12: Get Midterm and Final grades from a student for any course. 
# The sum of 40% of the midterm exam grade and 60% of the final grade will give the year-end average. 
# If the average is below 50, "FAILED" will appear on the screen, 
# and if it is 50 or above, "SUCCESSFUL" will be displayed on the screen. 
# This printing process is 4 lessons. and the lessons will be written one after the other.
lessons =[]
midterm =[]
final =[]
avareges =[]
for i in range(1,5):
    lesson = input ("inter a lesson name:")
    lessons.append(lesson)
    midterm_score = int(input("inter midterm score:"))
    midterm.append(midterm_score)
    final_score = int(input("inter final score:"))
    final.append(final_score)
    avarege = (midterm_score * 0.4) + (final_score * 0.6)
    avareges.append(avarege)
final_avg = sum(avareges)/4
if final_avg < 50:
    print(f"your final avarege is {final_avg} : FAILED")
else:
    print(f"your final avarege is {final_avg} :SUCCESSFUL")
