# For loop

1.Basics

for i in range(1,11):
   print(i)
    
word="Python"
for j in word:
    print(j)
    
word2="vivek"
for k in range(1,6):
    print(word2)


#2.loop using list

items=["pen","book","pencil"]
for item in items:
    print(item)
    
# Even number using loop
for i in range(2,21,2):
    print(i)

for i in range(1,20,2):
    print(i)

kill=[1,1,1,1,0]
total=0
for i in kill:
    total += i
print("total kills:",total)


#3.leading and trailing spaces removal
cities=['   MUMbai',  'KOlkatta','DELhI   ']
cleaned=[]
for m in cities:
    cleaned.append(m.strip().title())
print(cleaned)

4.identify Odd and Even number and print it in a list
data=[1,2,4,3,6,8,7,9,11,20,24,51,23,22,15]
for i in data:
    if i%2==0:
        print(i,"is Even Number")
    else:
        print(i,"is odd Number")

#5.extract last four digit of adhar id number from the give data
adhar=['xxxx2342222','xxxx73636636','xxxx36635353']
for id in adhar:
    print(id[-4:])

