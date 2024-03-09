import random

#card container
SUIT_TUPLE=('Spades','Heart','Clubs','dimonds')
RANK_TUPLE=('Ace','2','3','4','5','6','7','8','9','20','Jack','Queen','King')
NCARD=8

# pass in adeck and this function return a random card from the deck
def getcard(decklistIn):
    thiscard= decklistIn.pop()
    return thiscard

# pass in adeck and this function return a shuffled copy of the deck
def Shuffle(decklistIn):
    decklistOut=decklistIn.copy() # make copy of starting deck
    random.shuffle(decklistOut)
    return decklistOut

#Main code
print("Welcome to higher or lower.")
print("You have to choose whether the next card tobi shown will be higher or lower then the current card")
print("Getting it right adds 20 points ; get it wrong and you lose 15 points")
print("You have 50 point to start.")
print()

startingdecklist=[]  # dict which contain all card
for suit in SUIT_TUPLE:
    for thisvalue , rank in enumerate(RANK_TUPLE):
        carddict={'rank':rank,'suit':suit,'value':thisvalue +1}
        startingdecklist.append(carddict)
score=50

while True:
    print()
    gamedecklist=Shuffle(startingdecklist)
    currentcarddict=getcard(gamedecklist)
    currentcardrank=currentcarddict['rank']
    currentcardvalue=currentcarddict['value']
    currentcardsuit=currentcarddict['suit']
    print("Starting card is: " ,currentcardrank + " of "+ currentcardsuit)
    print()

    for carnnum in range(0 ,NCARD):
       answer=input('Will the next card be higher or lower then the'+
                 currentcardrank +"of"+
                 currentcardsuit + "? (enter h or l):")
       answer=answer.casefold() #force lowercase
       nextcarddict=getcard(gamedecklist)
       nextcardrank=nextcarddict['rank']
       nextcardvalue=nextcarddict['value']
       nextcardsuit=nextcarddict['suit']
       print("Next card is: ",nextcardrank + " of "+ nextcardsuit)
       print()
        
       if answer=='h':
           if nextcardvalue> currentcardvalue:
               print ("You got it was higher")
               score += 20
           else:
               print("Sorry , it was not higher")
               score-= 15
       elif answer=='l':
           if nextcardvalue < currentcardvalue:
               print ("You got it was lower")
               score += 20
           else:
               print("Sorry , it was not lower")
               score-= 15       
       print('Your score is:',score)
       print()
    goAgain = input('To play again, press ENTER , or "q" to quit')
    if goAgain == 'q':
        break   
    print('OK BYE')