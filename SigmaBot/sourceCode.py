def serverFarm(jobs, servers):
    
    # sort the jobs by their associated processing times in descending order 
    # assigns them to the server that's going to become available next.
        # If there are several servers with the same availability time, the algorithm assigns the job to the server with the smallest index.
        # If two operations have the same processing time, the one with the smaller index is listed first. 


    srvrs = [ list() for i in range(0,servers) ]  # holds server numbers
    serverTimes = [0]*servers               # holds server times
    
    jobTups = []
    
    i = 0
    x = len(jobs)
    while i < x:
        jobTups.append( [jobs[i], i] )
        
        i += 1
    
    jobTups.sort(key=lambda x: x[0] , reverse=True)
    
    #print(jobTups)
    i = 0
    while i < x:
        nextServer = serverTimes.index( min( serverTimes ) )
        srvrs[nextServer].append(jobTups[i][1])
        serverTimes[nextServer] += jobTups[i][0]
        i += 1
        
    return srvrs

    import datetime
    
def dailyOHLC(timestamp, instrument, side, price, size):
    
    # remember -- (timestamp, instrument) is a key
        # e.g. ("2015-12-20", "HPQ")
    
    # side and size are worthless in this problem
    
    # three parallel arrays
        # timestamps
        # instrument
        # price
    
    def createTuple(key, price):
        return [key[0], key[1], price, price, price, price]
    
    def insertTuple(tup):
        OHLC.append(tup)
        
    def updateTuple(index, price):
        if float(price) > float(OHLC[index][3]):
            OHLC[index][3] = price
            
        elif float(price) < float(OHLC[index][4]):
            OHLC[index][4] = price
            
        OHLC[index][5] = price
        
    def getTupleIndex(key):
        i = 0
        x = len(OHLC)
        y = key[0]
        z = key[1]
        while i < x:
            if OHLC[i][0] == y and OHLC[i][1] == z:
                return i
            i += 1
            
            
    timestamps = [ datetime.datetime.fromtimestamp( int(timestamp[i]) ).strftime('%Y-%m-%d') for i in
        range(0,len(timestamp)) ]
    
    keys = [] # these are all the doublets we come across
    
    OHLC = []
    
    i = 0
    x = len(timestamp)
    while i < x:
        key = (timestamps[i], instrument[i])
        
        p = str( format(price[i],'.2f') )       
        
        if key not in keys:
            keys.append(key)
            insertTuple( createTuple(key, p) )
        
        else:
            updateTuple( getTupleIndex(key), p )
            
        i += 1
    
    # now let's lexicographically order OHLC...
    OHLC.sort(key=lambda x: x[0]+x[1])
    
    
    return OHLC
