def countAPI(calls):
    # go through calls, fill out two maps: 
    # 1) hierarchy map: pathToParent (string) --> [pathToChild] (list of strings)
    # 2) count map: path (string) --> numberOfTimesPathEncountered (int)
    # also keep a list of the projects (to know the order in which to search)
    # go through highest level paths list, create list to output

    hierarchy = {}
    countMap = {}
    projectList = []
    projectSet = set()
    
    
    for call in calls:
        curCall = call.split('/')
        proj = '/' + curCall[1]
        subproj = proj + '/' + curCall[2]
        method = subproj + '/' + curCall[3]
        
        if proj not in projectSet:
            projectList.append(proj)
            projectSet.add(proj)
            hierarchy[proj], hierarchy[subproj] = [subproj], [method]
            countMap[proj], countMap[subproj], countMap[method] = 1, 1, 1
        else:
            if subproj not in hierarchy[proj]:
                hierarchy[proj].append(subproj)
            countMap[proj] += 1
            if subproj in countMap:
                if method not in hierarchy[subproj]:
                    hierarchy[subproj].append(method)
                countMap[subproj] += 1
            else:
                hierarchy[subproj], countMap[subproj] = [method], 1
            if method in countMap:
                countMap[method] += 1
            else:
                countMap[method] = 1
        
    API_Count = []
    for proj in projectList:
        API_Count.append('--' + proj[1:] + ' (' + str(countMap[proj]) + ')')
        subprojList = hierarchy[proj]
        for subproj in subprojList:
            API_Count.append('----' + subproj[len(proj)+1:] + ' (' + str(countMap[subproj]) + ')')
            methodList = hierarchy[subproj]
            for method in methodList:
                API_Count.append('------' + method[len(subproj)+1:] + ' (' + str(countMap[method]) + ')')
        
    return API_Count


def chatBot(conversations, currentConversation):
    # get matchInfo: (numMatches, largestMatchIndex) for each conversation, store them in a list
        # if numMatches == 0 for all, return currentConversation
    # compare conversations, starting from first one, and see which has greatest
    
    matchInfo = []
    currentConvoSet = set(currentConversation)
    
    for convo in conversations:
        numMatches = 0
        largestMatchIndex = -1
        matchedWords = set()
        for i in range(len(convo)):
            if convo[i] in currentConvoSet:
                if convo[i] not in matchedWords:
                    matchedWords.add(convo[i])
                    numMatches += 1
                largestMatchIndex = i
        matchInfo.append([numMatches, largestMatchIndex])
    
    mostMatches = -1
    index = -1
    for i in range(len(matchInfo)):
        if matchInfo[i][0] > mostMatches:
            mostMatches = matchInfo[i][0]
            index = i
    
    if mostMatches == 0:
        return currentConversation
    else:
        # should check if len(conversations[index]) > matchInfo[index][1]+1 for safety
        return currentConversation + conversations[index][(matchInfo[index][1]+1):]


def roadmap(tasks, queries):
    
    tasksSorted = sorted(tasks, key=lambda task: (task[2], task[0]))
    tasksForQueries = []
    
    for query in queries:
        tasksToComplete = []
        for task in tasksSorted:
            if task[1] <= query[1] <= task[2] and query[0] in task[3:]:
                tasksToComplete.append(task[0])
        tasksForQueries.append(tasksToComplete)
                
    return tasksForQueries

