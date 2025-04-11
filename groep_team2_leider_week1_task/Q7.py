# Question 7: 

seq = int(input("How many number you want ? "))
# first two terms
n1, n2 = 0, 1
count = 0
l=[0,1]
print(l)
# check if the number of terms is valid
if seq <= 0:
   print("Please enter a positive integer")
elif seq==1:
    print("Fibonaci sequence :")
    print(l[0])
else:
# if there is only one term, return n1
   print("Fibonacci sequence:")     
   while count < seq:
      
       nth = n1 + n2
       l.append(nth)
       # update values
       n1 = n2
       n2 = nth
       count += 1
print(l)