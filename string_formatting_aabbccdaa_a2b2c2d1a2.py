#user input string
s=input("Enter String \n")
#empty string to assign distinct  values as per format
lst=[]
#looping through range of values till length of user string
for i in range(len(s)):
    if i+1<len(s):
        if s[i]==s[i+1]:
            pass
        else:
            lst.append(s[i])
    elif i+1>len(s):
        lst.append(s[i])
    else:
        lst.append(s[i])
#two global variables initialized here
first_val=0
str_=""
#looping through appended values in list'
for x in lst:
    counter=0
#here, we loop each element untill it satisfy the condition and next it iterate from where exactly it got failed.
    for i in range(first_val,len(s)):
        if x==s[i]:
            counter+=1
            first_val+=1
        else:
            break
    str_+=x+str(counter)
print(str_)