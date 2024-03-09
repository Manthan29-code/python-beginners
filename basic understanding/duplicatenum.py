# problem:-
#print duplicate digite in given number
n=str(input("Enter the num"))
gate=list()
for i in n:
    sum=n.count(i,0,len(n))
    if sum>1 & (int(i) not in gate):
         gate.append(int(i))
print(set(gate))         