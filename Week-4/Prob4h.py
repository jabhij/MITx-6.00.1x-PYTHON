def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    maxScore = 0
    bestWord = None

    for word in wordList: 
        if isValidWord(word, hand, wordList) == True:
            wordScore = getWordScore(word, n)

            if wordScore > maxScore:
                maxScore = wordScore
                bestWord = word

    return bestWord

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
    """
    totalScore = 0
    while calculateHandlen(hand) > 0:
    
        print ('Current Hand: ' ), 
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)

        if word == None:
            print ('Total score: ' + str(totalScore) + ' points.')
            break
        else:
            totalScore = getWordScore(word, n) + totalScore
            print ('"' + str(word) + '"' + ' earned ' + str(getWordScore(word, n)) + ' points. Total: ' + str(totalScore) + ' points') 
                
        hand = updateHand(hand, word)
    if calculateHandlen(hand) == 0:
        print ('Total score: ' + str(totalScore) + ' points.')
    else:
        print ('  ')
        


