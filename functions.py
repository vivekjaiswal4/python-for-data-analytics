#FUNCTION:like machine or mini program
# takes a input perform set of operation or task and optionally return output
# imp for DA:
# reuse same logic multiple times
# clean data consistently
# improve project structure 
# make code readable & modular
# create reusable transformations
# essential for panda and real project

# two type of function-
# -pre define function 
# -user define function

# #syntax:
# def function_name():
#     code

# #function with no parameters
# def greet():
#     print("hello!,welcome!")
# #calling function
#     greet()

#Example:
# def greet():
#     print("Hello! How are You?")
#     reply=input("ans:")

# greet()
# 1.
def welcome(name):#parameter or argument when variable is assign in function name
    print("welcome",name)

welcome("satish")#argument: initialize the value in variable

#2.Arithmatic operations on a and b

# def arithmetic(a,b):

#     print("Addition:",a+b)
#     print("subtraction:",a-b)
#     print("Multiplication:",a*b)
#     print("division:",float(a/b))

# arithmetic(a=int(input("enter a:")),
# b=int(input("enter b:")))

#arithmatic by using Return
# def add(a,b):
#     return a+b
# sum=add(a=int(input("enter a:")),
# b=int(input("enter b:")))
# print(sum)

#print table using function
def table(a,b):
    for n in range(1,11):
        b=a*n
        return b

    
table(a=int(input("Enter a:")))
print(table)
