#in this file we have only define function
#use of this function is done in time.py
#ABOUT  __name__ variable
#it is inbuilt variable in python
#value of __name__ CASE 1) when file is called directly--> __main__
#                  CASE 2) when file is run in another file ---> __<name of file>__
from datetime import date
from datetime import datetime  

def currentdate():
    print(date.today())

def add(n1,n2):
    ans=n1+ n2
    print("addtion=",ans)

def currenttime():
    print(datetime.now()) 

print('hey from TIMEFUNCTION.PY')
if __name__== "__main__": # think why we need to write this logic
    print('File is being executed directly')
    print('value of __name__==',__name__)
    currentdate()
    add(4,40)
    currenttime()
else:
    print('File is imported in another file ')
    print('value of __name__==',__name__)
   
 
