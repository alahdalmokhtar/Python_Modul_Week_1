num=int(input("enter the positive num : "))
fact=1
if num > 0 :
    for i in range(1,num+1) :
        fact=fact*i
    print(f"the factrial for {num} : {fact}")
else:
    print("you can enter a positive number ")
