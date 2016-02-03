def biggest(aDict):

    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    
    getWord = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            getWord = key
            biggestValue = len(aDict[key])
    return getWord
