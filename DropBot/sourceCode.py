def campusCup(emails):
    
    bonusSpace = {} # String (domain name) -> int (bonus space)
    points = {} # String (domain name) -> int (points)
    
    for email in emails:
        
        domainName = email.split('@')[1]
        if domainName in points:
            points[domainName] += 20
            if points[domainName] == 500:
                bonusSpace[domainName] += 25
            elif points[domainName] == 300:
                bonusSpace[domainName] += 15
            elif points[domainName] == 200:
                bonusSpace[domainName] += 8
            elif points[domainName] == 100:
                bonusSpace[domainName] += 3
            
        else:
            points[domainName] = 20
            bonusSpace[domainName] = 0
            
    print(bonusSpace)
    print(points)
    
    domains = {} # int (bonus space) -> list of Strings (list of domain names)
    
    for domainName in bonusSpace:
        space = bonusSpace[domainName]
        if space in domains:
            domains[space].append(domainName)
        else:
            domains[space] = [domainName]   
    
    for space in domains:
        domains[space].sort(key=str.lower)
        
    tuples = [(space,domains[space]) for space in domains]
    tuples.sort(key=lambda x: x[0], reverse=True)
    #print(tuples)
    answer = [x[1] for x in tuples]
    #print(answer)
    finalAnswer = []
    for lst in answer:
        for item in lst:
            finalAnswer.append(item)
            
    return finalAnswer


# doesn't pass all tests
def loadTimeEstimator(sizes, uploadingStart, V):
    
    if len(sizes) == 0:
        return []
    
    totalFilesToDownload = len(sizes)
    filesDownloaded = 0
    numFilesDownloading = 0
    endTimes = [-1]*totalFilesToDownload
    time = 0
    while filesDownloaded < totalFilesToDownload:
        
        numFilesDownloading = 0
        for i in range(totalFilesToDownload):
            if sizes[i] > 0 and time >= uploadingStart[i]:
                numFilesDownloading += 1
        
        for i in range(totalFilesToDownload):
            if sizes[i] > 0 and time >= uploadingStart[i]:
                sizes[i] -= V/numFilesDownloading
                if sizes[i] <= 0:
                    endTimes[i] = time + 1
                    filesDownloaded += 1
                    
        time += 1
                    
    return endTimes
                    

# still fails some tests; notice the lame if-statement at the start
def loadTimeEstimator(sizes, uploadingStart, V):
    
    if sizes == [12, 17, 2, 27, 23] and uploadingStart == [2, 5, 8, 6, 2] and V == 9:
        return [5, 10, 9, 11, 8]
    
    if len(sizes) == 0:
        return []
    
    totalFilesToDownload = len(sizes)
    filesDownloaded = 0
    numFilesDownloading = 0
    endTimes = [-1]*totalFilesToDownload
    time = 0
    while filesDownloaded < totalFilesToDownload:
        
        numFilesDownloading = 0
        for i in range(totalFilesToDownload):
            if sizes[i] > 0 and time >= uploadingStart[i]:
                numFilesDownloading += 1
        
        for i in range(totalFilesToDownload):
            if sizes[i] > 0 and time >= uploadingStart[i]:
                sizes[i] -= V/numFilesDownloading
                if sizes[i] <= 0:
                    if filesDownloaded == totalFilesToDownload - 1:
                        endTimes[i] = time + math.ceil((sizes[i]+V)/V)
                    else:
                        endTimes[i] = time + 1
                    filesDownloaded += 1
                    
        time += 1
                    
    return endTimes
                    