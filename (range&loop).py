#l.LOOP + RANGE
# print 1 to 5
# for i in range(1,6):
#     print(i)

# #print even numbers  from 1-18
# for i in range(2,19,2):
#     print(i)
# #print odd numbers from 1-18
# for i in range(1,18,2):
#     print(i)

# #count from from 10 t0 1
# for i in range(10,0,-1):
#     print(i)

# #loop through list using index
# items=["pen","pencil","scale"]
# for i in range(len(items)):
#     print(i,items[i])

# #generate employee id
# for i in range(1,6):
#     print("EMP-",i)

# #create list of years
# years=[]
# for i in range(2014,2027):
#     years.append(i)
# print("years of bjp government ruling:",years)

#clean cities spaces and font using loop and list
cities=["   MUmBai","PuNe    ","  DelHI    "]
cleaned=[]
for i in cities:
  cleaned.append(i.strip().title())
print(cleaned)

#Extract last 4 digit from list
employees=["vivek-2008","shubham-2009","abhishek-2003"]
for i in range(len(employees)):
  print(employees[i][-4:])

#nested  for loop
for i in range(1,4):
  for j in range(1,4):
    print(i,j)