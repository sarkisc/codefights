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




from datetime import datetime

def busyHolidays(shoppers, orders, leadTime):
    
    if len(shoppers) < len(orders):
        return False
    
    # for each order, figure out which shopper(s) can take the order
    # 
    # 
    # didn't do these things
    # if there exists an order that no shopper can take:
        # return False
    # if len(eligible_shoppers) < len(orders):
        # return False
    # 
    # 
    # permute through eligible shoppers for each order until a "good" combination is found
        # return True
    # if no "good" combination is found:
        # return False
    
    shoppers_for_orders = [[] for i in range(len(orders))]

    for i in range(len(orders)):
        for j in range(len(shoppers)):
            if canTakeOrder(orders[i], shoppers[j], leadTime[i]):
                shoppers_for_orders[i].append(j)
    
    #print(shoppers_for_orders)
    
    sets = [set([num]) for num in shoppers_for_orders[0]]
    i = 1
    while i < len(orders) and sets != []:
        sets = getNextLevel(sets, shoppers_for_orders[i], i+1)
        i += 1
    
    if sets == []:
        return False
    return True
    

#helper
def getNextLevel(sets, shoppers, desiredLength):
    newSets = []
    for st in sets:
        for shopper in shoppers:
            newSet = set(st)
            newSet.add(shopper)
            if len(newSet) == desiredLength:
                newSets.append(newSet)
    return newSets
    

# can shopper complete order? returns bool
def canTakeOrder(order, shopper, leadTime):
    
    Ss = dt(shopper[0])
    Se = dt(shopper[1])
    Os = dt(order[0])
    Oe = dt(order[1])
    
    if Ss > Oe:
        return False
    
    shopperTime = -1
    if Ss <= Os:
        if Se <= Oe:
            shopperTime = Se - Os
        else:
            shopperTime = Oe - Os
    else:
        if Se <= Oe:
            shopperTime = Se - Ss
        else:
            shopperTime = Oe - Ss
    
    if shopperTime >= leadTime:
        return True
    return False


# returns difference between two times in minutes
# time1 must come after time2
def dt(time1, time2="00:00"):
    frmt = '%H:%M'
    t1 = datetime.strptime(time1, frmt)
    t2 = datetime.strptime(time2, frmt)
    return (t1-t2).total_seconds() / 60
    