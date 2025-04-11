#Quetion 12
total_les=1
sum=0
while total_les <=4 :
    print(f"\nCourse {total_les}")
    les1=input(f"enter the course name : ")
    midterm=int(input(f"enter the midter for course{total_les} :"))
    final_grade=int(input(f"enter the final grade for course{total_les}:"))
    total_les +=1
    avg=(midterm*.4)+(final_grade*.6)
    if avg >=50 :
        status="Succful "       
    else:
        status="Faild"
    print(f"the course : {les1} - Average : {avg}  is {status}")