def memoize(f):
    memo = {}
    def helper(x, y):
        if (x,y) not in memo:            
            memo[(x,y)] = f(x,y)
        return memo[(x,y)]
    return helper
    
def theFile(version1, version2):
    if len(version1) == 0 or len(version2) == 0:
        return ""
    
    else:

        lst = []

        for i in range(len(version1)):
            for j in range(len(version2)):
                if version1[i] == version2[j]:
                    final_answer = ""
                    final_answer += version1[i]
                    final_answer += theFile(version1[i+1:], version2[j+1:])
                    lst.append(final_answer)
        
        return max(lst, key=lambda x: len(x))
    
theFile = memoize(theFile)



def segmentDeletionSlow(left, right):

    toRemove = len(left)
    tups = set()
    lst = []
    
    for i in range(len(left)):
        x = (left[i], right[i])
        tups.add(x)
        lst.append(x)
    
    numTups = []
    for tup in tups:
        numTups.append(lst.count(tup))
        
    for num in numTups:
        if num > 1:
            toRemove -= num
    
    print(toRemove)

    ranges = []
    
    for tup in tups:
        ranges.append(list(range(tup[0], tup[1]+1)))
    
    print(ranges)
    
    for i in range(len(ranges)):
        for j in range(len(ranges)):
            if set(ranges[i]) < set(ranges[j]):
                toRemove -= 1
                 
    return toRemove




import math
def smallestPalindrome(s0):
    
    table = set()
    LP, RP = 0, 0
    
    if len(s0)%2 == 0:
        LP, RP = len(s0)//2 - 1, len(s0)//2
    else:
        LP, RP = len(s0)//2, len(s0)//2
    
    fillTable(table, s0, LP, RP)
    
    # then find the lexicographically smallest palindrome
    print(table)
    diff = [item for item in table if item >= s0]
    return min(diff)
    
            
def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False


def fillTable(tbl, stg, LP, RP):
    if LP == -1 or isPalindrome(stg):
        tbl.add(stg)   
    else:
        # create the two new strings
        newStrs = formStrings(stg, LP, RP)
        for stg in newStrs:
            if isPalindrome(stg):
                tbl.add(stg)
        LP -= 1
        RP += 1
        # call fillTable on both
        fillTable(tbl, newStrs[0], LP, RP)
        fillTable(tbl, newStrs[1], LP, RP)

def formStrings(stg, LP, RP):
    # 'z' should become 'a' and 'z'
    if stg[LP] == 'z' and stg[RP] == 'z':
        newStr1 = stg
        newStr2 = stg[0:LP] + 'a' + stg[LP+1:RP] + 'a' + stg[RP+1:] 
    elif LP == RP:
        tmp = ord(stg[LP])
        tmp += 1
        newStr1 = stg[0:LP] + chr(tmp) + stg[LP+1:]
        newStr2 = stg
    elif LP == RP - 1:
        tmp1 = ord(stg[LP])
        tmp2 = ord(stg[RP])
        z = abs(tmp1-tmp2)
        if z == 1:
            newStr1 = stg[0:LP+1] + stg[LP] + stg[RP+1:] 
            newStr2 = stg[0:LP] + stg[RP] + stg[RP:]      
        elif z == 0:
            x = tmp1 + 1
            newStr1 = stg[0:LP+1] + stg[LP] + stg[RP+1:]
            newStr2 = stg[0:LP] + chr(x) + chr(x) + stg[RP+1:]
        else:
            x = min(tmp1, tmp2) + 1
            y = max(tmp1, tmp2)
            newStr1 = stg[0:LP] + chr(x) + chr(x) + stg[RP+1:]
            newStr2 = stg[0:LP] + chr(y) + chr(y) + stg[RP+1:]       
    else:
            tmp1 = ord(stg[LP])
            tmp2 = ord(stg[RP])
            x = min(tmp1, tmp2)
            y = max(tmp1, tmp2)
            newStr1 = stg[0:LP] + chr(x) + stg[LP+1:RP] + chr(x) + stg[RP+1:]
            newStr2 = stg[0:LP] + chr(y) + stg[LP+1:RP] + chr(y) + stg[RP+1:] 

    return [newStr1, newStr2]
        
        
        

def semiprimeByNumber(n):
    print(generateSubprimes())
    return generateSubprimes()[n-1]

    
    
def generatePrimes():
    primes = set({2,3,5,7})
    for i in range(11,98):
        isPrime = True
        for j in range(2,10):
            if i%j == 0:
                isPrime = False
        if isPrime:
            primes.add(i)
    return primes

def generateSubprimes():
    primes = generatePrimes()
    subprimes = set()
    for prime1 in primes:
        for prime2 in primes:
            subprimes.add(prime1*prime2)
    SP = list(subprimes)
    SP.sort()
    return SP




def chipMoving(grid):
    width = len(grid[0])
    height = len(grid)
    
    grd = makeGrid(width, height)
    
    # take care of top row and leftmost column first
    grd[0][0] = (0, 'X')
    for i in range(1, width):
        grd[0][i] = (grd[0][i-1][0]+grid[0][i], 'R')
    for j in range(1, height):
        grd[j][0] = (grd[j-1][0][0]+grid[j][0], 'B')
    for i in range(1, height):
        for j in range(1, width):
            
     
def makeGrid(width, height):
    grd = []
    for j in range(0, height):
        grd.append([0]*width)
    return grd



def periodicSequence(s0, a, b, m):
    sequence = [s0]
    for i in range(1,101):
        curInt = sequence[-1]
        tmp = (a*curInt + b)%m
        sequence.append(tmp)
    
    #print(sequence)
    
    dct = {}
    for i in range(len(sequence)):
        if sequence[i] not in dct:
            dct[sequence[i]] = i
        else:
            return i - dct[sequence[i]]
        



# passes CF tests, but I came up with tests it fails...
def zigzag(a):
    maxLen = 1
    curLen = 1
    fns = [lessThan, greaterThan]
    
    i = 1
    fnIndex = init(a, i)
    fn = fns[fnIndex]
    while i < len(a)-1:
        if fn(a[i], a[i-1]):
            curLen += 1
            if fn(a[i], a[i+1]):
                curLen += 1
                fnIndex = alternate(fnIndex)
                fn = fns[fnIndex]
            else:
                if curLen > maxLen:
                    maxLen = curLen
                curLen = 1
                fnIndex = init(a, i+1)
                fn = fns[fnIndex]
        else:
            if curLen > maxLen:
                maxLen = curLen
            curLen = 1
            fnIndex = init(a, i+1)
            fn = fns[fnIndex]
        
        i += 1
        
    return maxLen//2+1
        

def lessThan(x, y):
    return x < y

def greaterThan(x, y):
    return x > y

def init(a, index):
    if lessThan(a[index], a[index-1]):
        return 0
    return 1
    
def alternate(num):
    if num == 0:
        return 1
    return 0


# fixed, but untested -- should work
def zigzag(a):
    maxLen = 1
    curLen = 1
    fns = [lessThan, greaterThan]
    
    i = 1
    fnIndex = init(a, i)
    fn = fns[fnIndex]
    while i < len(a)-1:
        if fn(a[i], a[i-1]):
            curLen += 1
            if fn(a[i], a[i+1]):
                curLen += 1
                fnIndex = alternate(fnIndex)
                fn = fns[fnIndex]
            else:
                if curLen > maxLen:
                    maxLen = curLen
                curLen = 1
                fnIndex = init(a, i+1)
                fn = fns[fnIndex]
        else:
            if curLen > maxLen:
                maxLen = curLen
            curLen = 1
            fnIndex = init(a, i+1)
            fn = fns[fnIndex]
        
        i += 1
        
    if fn(a[i], a[i-1]):
        curLen += 1
    if curLen > maxLen:
        maxLen = curLen
        
    return maxLen//2+1
        
        

def lessThan(x, y):
    return x < y

def greaterThan(x, y):
    return x > y

def init(a, index):
    if lessThan(a[index], a[index-1]):
        return 0
    return 1
    
def alternate(num):
    if num == 0:
        return 1
    return 0