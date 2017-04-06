def ratingThreshold(threshold, ratings):
    
    nums = []
    
    i = 0
    x = len(ratings)
    while i < x:
        y = sum(ratings[i]) / len(ratings[i])
        if y < threshold:
            nums.append(i)

        i += 1


    return nums

    def proCategorization(pros, preferences):
    
    jobs = []
    
    # insert in jobs the following: tuples of the form [ [job], [people who do the job] ]
        # e.g. [ ["Computer repair"], ["Jack, "Leon"] ]
    
    def check(job):
        for tup in jobs:
            if tup[0][0] == job:
                return jobs.index(tup)
        return -1
    
    def insertPro(index, pro):
        jobs[index][1].append(pro)
    
    i = 0
    x = len(pros)
    while i < x:
        y = pros[i]
        for job in preferences[i]:
            z = check(job)
            if z == -1:
                jobs.append([[job],[y]])
            else:
                insertPro(z,y)
        
        i += 1
        
    jobs.sort(key=lambda x: x[0][0])
    
    for job in jobs:
        job[1].sort()
    
    return jobs