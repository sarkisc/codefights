def delivery(order, shoppers):
    
    storeDistance = order[0]
    receiveGrocTime = order[1]
    waitTime = order[2]
    
    shopperTimes = []
    
    for shopper in shoppers:
        timeToFulfillOrder = (storeDistance + shopper[0])/shopper[1] + shopper[2]
        shopperTimes.append(timeToFulfillOrder)
        
    
    def takeOrder(shopperTime):
        idleMinutes = receiveGrocTime - shopperTime
        if idleMinutes <= 0 and idleMinutes >= -1*waitTime:
            return True
        return False
    
    takeOrderOrNot = []
    
    for shopperTime in shopperTimes:
        takeOrderOrNot.append(takeOrder(shopperTime))
        
    return takeOrderOrNot
        

def isAdmissibleOverpayment(prices, notes, x):
    
    # parse notes:
    # if second word is "higher":
        # add percentage to amountOverInStore
    # elif second word is "lower":
        # subtract percentage from amountOverInStore
    # compare amountOverInStore and x
    # (if x is greater, return true...else return false)
    
    
    def parseString(note):
        theNote = str(note)
        return theNote.split(" ", 2)
    
    amountOverInStore = 0
    
    #parsedStrings = []
    #percentages = []
    rates = []

    i = 0
    while i < len(prices):
        #parsedStrings.append( parseString(notes[i]) )
        lst = parseString(notes[i])
        
        curPrice = prices[i]
        
        if lst[0] != "Same":
            rate = float( lst[0].split("%")[0] )*0.01
        
        #rates.append(rate)
        
        if lst[1] == "higher": 
            origPrice = curPrice / (1+rate)
            amountOverInStore += (curPrice - origPrice)
        elif lst[1] == "lower":
            origPrice = curPrice / (1-rate)
            amountOverInStore += (curPrice - origPrice)
    
        i += 1
    
    
    if abs(x - amountOverInStore) < 0.0000001 or x >= amountOverInStore:
        return True
    return False
