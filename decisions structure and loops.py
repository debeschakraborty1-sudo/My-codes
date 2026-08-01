'''1.n= int(input("enter a number:"))
for i in range(1,n+1):
    print("square of",i,"=",i*i)'''

'''2.start=int(input("enter starting number:"))
end=int(input("enter ending number:"))
for i in range(start,end+1):
    print("square of",i,"=",i*i)'''

'''3.num=int(input("enter the number:"))
temp=num
digits=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit*digits
    temp//=10
if sum==num:
    print("armstrong number")
else:
    print("not an armstong number")'''

'''4.num=int(input("enter a number:"))
temp=num
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp//=10
if reverse==num:
    print("palindrome number")
else:
    print("not a palindrome number")'''

'''5.num=int(input("enter a number:"))
temp=num
sum=0
product=1
while temp>0:
    digit=temp%10
    sum+=digit
    product*=digit
    temp//=10
if sum==product:
    print("spy number")
else:
    print("not a spy number")'''

'''6.p=float(input("enter principal amount:"))
t=float(input("enter time(years):"))
r=float(input("enter rate of interest:"))
amount=p*(1+r/100)**t
ci=amount-p
print("compound interest=",ci)
print("total amount=",amount)'''

'''7.text=input("enter a string:")
vowels=0
consonents=0
digits=0
for ch in text:
    if ch.isdigit():
        digits+=1
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonents+=1
print("vowels=",vowels)
print("consonents=",consonents)
print("digits=",digits)'''

'''8.n=int(input("enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
print()'''

n=int(input("enter no of rows:"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
print()        
    

    
