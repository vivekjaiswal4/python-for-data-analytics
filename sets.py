#SETS 
# unorderd,mutable,and unique values only
# application for DA:
# remove duplicate values,extracrt unique values from columns


#Create sets -{}
# fruits={"apple","banana","apple","mango"}
# print(fruits)
# #remove duplicates values like apple is csalled sets

# #Adding
# fruits.add("orange")
# print(fruits)

# #Deleting
# fruits.discard("banana")
# print(fruits)

# #sets operations 
# a={1,2,3,4}
# b={4,5,6}
# print("Union:",a | b)  #combine both the sets 
# print("Intersection:",a & b)  #shows only common values
# print("Difference:",a - b)  #shows values that is uncommon columb written first eg A i.e 1,2,3
# print("Symmetric Difference:",a ^ b)  #shows values both sets without repeated item eg remove 4 that is common in both sets is remove

# #Remove Duplicates  --real apllication in DA
# cities={"Mumbai","Delhi","Pune","Delhi"}
# unique_cities=set(cities)
# print("Unique Cities:",unique_cities)


# #2.Common skills
# depA={"SQL","Python","Excel"}
# depB={"Power BI","SQL","Scikit"}
# common_skills=set(depA & depB)
# print("common skills:",common_skills)

# #3.Missing skills
# missing=set(depA-depB)
# print("MISSING SKILLS OF DEPARTMENT B:",missing)