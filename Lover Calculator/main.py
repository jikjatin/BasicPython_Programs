# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
comb_name=name1 + name2
low_name=comb_name.lower()
t=low_name.count('t')
r=low_name.count('r')
u=low_name.count('u')
e=low_name.count('e')
l=low_name.count('l')
o=low_name.count('o')
v=low_name.count('v')
e=low_name.count('e')
sum1=t+r+u+e
sum2=l+o+v+e
res=sum1*10+sum2 #or sum=int(sum1+sum2)
if res<10 or res>90:
 print(f"Your score is {res}, you go together like coke and mentos.")
elif res>40 and res<50:  
 print(f"Your score is {res}, you are alright together.")
else:
 print(f"Your score is {res}.")
