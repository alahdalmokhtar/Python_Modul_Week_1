num=int(input("enter the num : "))
if num > 1:
    for i in range(2,num):
         if num % i==0:
              print("not prime ")
              break
    else:
              print("this number is prime.")
            
else:
     print("this number  not prime .")