from random import randint
list=[[' ',' ',' '] for i in range(3)]

def display_board():
    global list
    print('CURRENT CONDITION OF BOARD')
    for i in list:
        print(i)

def AI_board():
    global list
    x=randint(0,2) 
    y=randint(0,2)
    if  list[x][y] !=' ':
        while list[x][y] !=' ':
             x=randint(0,2) 
             y=randint(0,2)
        list[x][y] ='0'
    else:
        list[x][y] ='0'

def human_board():
    global list
    print('select your location to place * ')
    x=int(input('enter number for row'))
    
    while x not in range(0,3):
      x=int(input('enter number for row'))
    y=int(input('enter number for column'))    
   
    while y not in range(0,3):
      y=int(input('enter number for column'))
    
    if list[x][y] !=' ':
        
         while list[x][y] !=' ':
            print('select your proper location to place * ')
            x=int(input('enter number for row'))
            
            while x  not in range(0,3):
              x=int(input('enter number for row'))
            y=int(input('enter number for column'))    
            while y not in range(0,3):
              y=int(input('enter number for column'))
         list[x][y]='*'
    
    else:
         list[x][y]='*'

i=1
while True:
    display_board()
    human_board()
    i+=1
    if i==5:
        break
    AI_board()
display_board()