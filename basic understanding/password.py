#question---> take password from user and print is it week, medium or strong

password=input("ENter password")
upper=0
lower=0
digit=0

for c in password:
    if c.isupper() == True:  # here we are using UDF 
        print(c)
        upper += 1  

    if c>='a' and c<='z': # here we are relational operator
        print(c)
        lower+=1
    if c>='0'and c<='9' :
        digit+=1
print(upper)
print(lower)
print(digit)
if len(password)<8 or upper==len(password) or lower==len(password) or digit==len(password) :
    print("weak password")
elif len(password)>=8 and (upper==0 or lower==0 or digit==0):
    print("Normal password")
else:
    print("Strong passwprd")    