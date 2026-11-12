# While loop
# Syntax
# while condition:
#     statement to repeat

#1.Basic while loop

# i=1
# while i<=5:
#     print(i)
#     i+=1

#2.countdown from 10 to 1

# n=10
# while n>0:
#     print(n)
#     n-=1

# 3.Ask user until valid input 
# num=""
# while not num.isnumeric():
#     num=input("Enter any number:")
#     print("Enter number only!")
# print("Number accepted: ",num)

# # 4.loop using list
# item=["Apple","banana","chickoo"]
# i=0
# while i<len(item):
#     print(item[i])
#     i+=1

# 5.print until 5 reach and stop Using BREAK
#USING FOR LOOP
# for n in range(1,10):
#     if n==5:
#         break
#     print(n)
#USING WHILE LOOP
# n=1
# while n<10:
#     if n==5:
#         break
#     print(n)
#     n+=1
    
#6. Using CONTINUE print odd numbers between 1-10
# y=0
# while y<10:
#     y+=1
#     if y%2==0:
#         continue
#     print(y)

#Even numbers
# y=0
# while y<10:
#     y+=1
#     if y%2==1:
#         continue
#     print(y)
# z=1
# while z<=10:
#     z+=1
#     if z%2!=0:
#         continue
#     print(z)

# z=0
# while z<10:
#     z+=1
#     if z%2!=1:
#         continue
#     print(z)

#7.Password System Advanced
password=""
attempts=0
while password!="Admin" and attempts<3:
    password=input("Enter Password:")
    attempts+=1
    if password=="Admin":
        attempts=0 
        print("Login Successfully!")
        break
    else:
        remain=3-attempts
        print("Wrong Password!")
        print("Warning!:You have",remain,"Attempts left")
        if remain==0:
            print("Dont panic !!!,Attempt is Expired Come after 1 hour")
        continue

