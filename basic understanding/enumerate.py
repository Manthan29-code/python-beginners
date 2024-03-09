l1={"eat","code","sleep"}
fruits={"apple","bannana", "watermelon"}

# enumerator in use to assign noumber to elvry element of iterable data type
# it take two argument 1)iterable 2) starting index (default value=0)
#it return enum object which is iterable
l2=enumerate(l1)   
print(l2)
print(type(l2))

for ele in enumerate(l1):
    print(ele)
for no,ele in enumerate(fruits,100):
    print(no,ele)

dictionary={fruit:no for no,fruit in enumerate(fruits)}
print(type(dictionary))
print(dictionary)