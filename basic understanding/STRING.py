#%%
#positive index 
s ="Hi,my name is Manthan"
print("Type of s is",type(s))
print(s)  #to print whole string
print(s[6])  # to print element at index 6
print("Length of string is= ",len(s))  # len(s) reaturn length of object s
print(s[0:6])  # ilterate from index 0 to 5
print(s[3:9])   #s[strating : ending: steps ]
for i in range(0,5): # i= 0 to 4
    print(s[i],end="")   
print("\n",s[0:len(s):3])  #s[strating : ending : steps ]

#%%
# about the negative index
'''
In this type of indexing pythin autometicaly 
add len(string) befor negative sign  for example......
'''
s ="Hi,my name is Manthan"
print(s[-3]) # python will understand it as print(s[len(s)-3])
            # so  it is equal to print(s[11]) if len(s) is 14
print(s[20:len(s)])
print(s[-10:-2:2])
print(s[-len(s):-1])
print(s[::-5])
#%%
#In-built functian that we can use with string object
upper_count=0
lower_count=0
s ="Hi,my name is Manthan"
for c in s:
    if c.isupper():   # return true is c is upper case
        upper_count+=1
    if c.islower():  # return true is c is lower case
        lower_count+=1
        
print("Totle no of upper case letter in s=",upper_count)     
print("Totle no of upper case letter in s=",lower_count)     

print(s.upper()) #Return a "copy" of the string converted to uppercase
print(s.lower()) #Return a "copy" of the string converted to lowercase

# to find index of specific element for first occurence
print(s.index('m'))

list=[]
list=s.split()
print(list)

print(s.count('a'))


# %%
# arithmetic aperation on string

s1="Manthan"
s2=" Movaliya"
s3= s1 + s2
print(s3)
print(s1*3)
print(ord('A'))  # ord reaturn ascill value

# %%
