hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}    

#this problem is to find how many letter word in hand.


def displayHand(hand):
    my_list= []
    for key in hand.keys():
        l = key * hand[key]
        l2 = list(l)
        my_list.append(l2)
        ''.join(my_list)
    return my_list

print displayHand(hand)




def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
   

        
        
        
        
        
        
        
        