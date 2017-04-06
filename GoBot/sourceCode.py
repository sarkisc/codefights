def domainType(domains):
    
    descriptions = []
    
    for domain in domains:
        if domain.endswith(".com"):
            descriptions.append("commercial")
        elif domain.endswith(".net"):
            descriptions.append("network") 
        elif domain.endswith(".org"):
            descriptions.append("organization")
        elif domain.endswith(".info"):
            descriptions.append("information") 
            
    return descriptions


def domainForwarding(redirects):

    # these are just notes...they are not necessarily representative of my solution
    
    # initialize a directed graph
    # figure out ENDs of graph, see from which nodes you can reach each END
        # ENDs exist in second column of redirects, but not in first column
    
    # remember -- each node has an END node associated with it
        # the END node associated with an END node is...itself :)
        # figure out each node's associated END node
            # make list of all redirect[0] 's
                # check if its associated redirect[1] is in the list of redirect[0] 's
                    # if so, keep going...
                    #
                    # if not, you've found the END node associated with a particular redirect[0]
    
    # then sort strings lexicographically
    
    def find(curNode):
        for red in redirects:
            if red[0] == curNode:
                return redirects.index(red)
        return -1
    
    def find2(string):
        if string in lexSorted:
            return lexSorted.index(string)
    
    nonEndNodes = []
    for red in redirects:
        nonEndNodes.append(red[0])
    
    end = []
    for red in redirects:
        curNode = red[1]
        x = find(curNode)
        while x != -1:
            curNode = redirects[x][1]
            x = find(curNode)
        end.append(curNode)
    
    # lex sort them
    lexSorted = []
    for item in end:
        if item not in lexSorted:
            lexSorted.append(item)
    lexSorted.sort(key=str.lower)
    
    lists = [[lexSorted[i]] for i in range(0,len(lexSorted))]
    
    # group them
    i = 0
    while i < len(end):
        x = find2(end[i])
        lists[x].append( redirects[i][0] )
        i += 1
    
    for lst in lists:
        lst.sort(key=str.lower)
        
    return lists