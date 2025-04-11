user_wrd=input("enter the word you want to reverse :")
reverse_wrd=user_wrd[::-1]
print(reverse_wrd)
#========Andere manier =============
rev=" "
for i in user_wrd:
    rev=i +rev
print(rev)