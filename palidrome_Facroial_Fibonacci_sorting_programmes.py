#palindorme
s=int(input("enter number for reve \n"))
actual_num=s
rev_num=0
while s!=0:
    remainder=s%10
    rev_num=rev_num*10+remainder
    s=s//10
if actual_num==rev_num:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

#Factorial
a=int(input("enter number for factorial\n"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)

#Fibonacci
b=int(input("enter number for fibonacci\n"))
num1,num2=0,1
counter=0
while counter<b:
    print(num1)
    num=num1+num2
    num1=num2
    num2=num
    counter+=1


#sorting programme
b=input("enter numeric/apha/alphanumeric \n")
str_=[x for x in b]
counter=0
while counter<len(str_):
    for i in range(len(str_)):
        if i+1<len(str_):
            if str_[i]>str_[i+1]:
                str_[i],str_[i+1]=str_[i+1],str_[i]
            else:
                pass
        elif i+1>len(str_):
            pass
    counter+=1
print("".join(str_))

str1_=""
num1_=""
for i in str_:
    if i.isnumeric():
        num1_+=i
    elif i.isalpha():
        str1_+=i
print(str1_+num1_)
            
       

    



    
    

