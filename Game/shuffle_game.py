from random import shuffle

# first, we define function for shufffliing 
def shuffler(list):
   shuffle(list)
   return list

# this function is defined to take number from user

def guess():
    guess_no=None
    while guess_no not in [0,1,2]:
        guess_no=int(input("chooes a number from 0,1,2"))
    return guess_no

# function to check that number chosen by the user is indicate the right position of bowle after shuffling or not

def check(list_bowle,num):
    
    if list_bowle[num]=='0':
        print('correct !')
    else:
        print('You guess wrong number' )
        print('right position of bowle')
        print(list_bowle)

key=1
while key==1:
    list=['0','','']
    print('This is position of bowle before shuffling')
    print(list)
    list_new=shuffler(list)
    number=guess()
    check(list_new,number)
    key=int(input('If you want to play game again then enter 1 ,otherwise enter 0'))


