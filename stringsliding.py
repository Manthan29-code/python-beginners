s ="Hi,my name is Manthan"
print(s)
print(s[6])
print(len(s))
print(s[0:len(s)])
print(s[3:9])   #s[strating : ending ]
for i in range(0,len(s)):
    print(s[i],end="")
print("")    
print(s[0:len(s):3])  #s[strating : ending : steps ]   
# about negative index
print(s[-3])
print(s[-1:-(len(s))])
print(s[-10:-2:2])
print(s[-len(s):-1])
print(s[0::-5])