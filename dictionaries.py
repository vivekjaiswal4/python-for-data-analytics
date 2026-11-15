#DICTIONARIES
#Dictionary is like a real dictionary book:
# unordered,mutable an written in parenthesis{} like json file 
# application for DA:
# store structered data 
# store column wise data(like json)
# used in APIs,json files database results
# use in pandas

#Basics
student={
    "name":"vivek","age":18,"city":"Mumbai"
}
# print(student)

#Accessing Elements/Searching
# print("what is name of student?:",student["name"])
# print("city he lives?:",student["city"])

#Adding or updating
# student["city"]="Gurugram"
# student["age"]=20
# print(student)

# #Removing or deleting
# student.pop("city")
# print(student)

#Dictionaries Methods
# print(student.keys())  #shows only name,age,city i.e attributes of dictionary
# print(student.values()) #shows values stored in keys or attributes like name:vivek i.e show vivek only not name
# print(student.items())  #show both keys and values overall items
# print(student.get("name")) #shows only desired values of particular key

#Looping
# for k in student:
#     print(k,student[k]) #k prints keys of student dictionary and student[k] prints values stored in key

#Nested Dictionary -dictionaries under dictionary.
# employees= {
#     "emp101":{"name":"sumit","age":18},
#     "emp102":{"name":"priyam","age":20}
# }
# print(employees)
# print(employees["emp101"]["name"]) #print(Dictionary["sub-dictionary"]["key of sub-dictionary"])

#mapping wrong -> correct
mapper ={ "dilli":"delhi","panjab":"punjab"
}
print(mapper["dilli"])
