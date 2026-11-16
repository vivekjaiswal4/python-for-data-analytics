#Tuples
# Tuples=():store not changable values
# applications for DA:stores fix values
# prevent accidental modifications
# stores coordinates
# store values that should not change in code
# faster than list 
# used in CSV rows returned by database fetch operations
# used in pandas.itertuples()

#basics-create tuples
fruits=("apple","banana","mango")
print(fruits)

#indexing
print(fruits[-1:])
print(fruits[0])

#slicing
nums=(10,20,30,40,50)
print(nums[3:])
print(nums[-3:])

#looping
colors=("red","blue","green")
bind=()
for c in colors:
    print(c)

#length
print(len(colors))

#concatenation
a=(1,2)
b=(3,4)
print(a+b)

#packing and unpacking
players=("rusher","sniping","survival")
omkar,shubham,abhishek=players
print(f"rusher:{omkar} sniping:{sh}")

