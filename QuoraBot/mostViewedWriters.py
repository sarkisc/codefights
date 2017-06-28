def mostViewedWriters(topicIds, answerIds, views):
    
    # iterate over topicIds (topics are 1-indexed) (1 <= topicId <= 1000)
        # topicIds shows the topics associated with ith question (questions are 0-indexed)
        # look in answerIds to figure out answerId corresponding to the questions found in previous step
        # for reach answerId found in previous step, 
            # find it as the first elem of a triple in views
            # take the second two elems of the triple in views and put it in your answer
                # if any future insertions have same userId, add views
                    # look at topicId = 4 as an example: 
                        # [1,2] already in mostViewedWriters(3), trying to insert [1,1] ==> [1,3]
                # if any insertions have views == 0, don't insert
    
    # sort the tuples in the result based on views
        # tie goes to user with smaller userId (write separate key function)

    theAnswer = []
    
    # lst is of the form [ views[i][k] , views[i][j] ]
    def initializeTuple(lst):
        return [lst]
        
    def insertTuple(tup):
        theAnswer.append(tup)
        
    # ID is just curTopicId
    def findTuple(key):
        i = 0
        x = len(theAnswer[len(theAnswer)-1])
        while i < x:
            
            if theAnswer[len(theAnswer)-1][i] == key:
                return i
            
            i += 1
        
        return -1
    
        
    curTopicId = 1
    while curTopicId < 1001:
        
        keys = set()
        answers = []
        questions = []
        
        i = 0
        x = len(topicIds)
        while i < x:
            if curTopicId in topicIds[i]:
                questions.append(i)
            i += 1
            
        for answer in questions:
            y = answerIds[answer]
            for item in y:
                answers.append(item)
        
        for view in views:
            if view[0] in answers:
                key = view[1]
                value = view[2]
                if key in keys:
                    theAnswer[len(theAnswer)-1][findTuple(key)][1] += value
                else: 
                    keys.add(key)
                    insertTuple( initializeTuple( [key, value] ) )
            
        
        curTopicId += 1


    print(theAnswer)
    #return theAnswer
