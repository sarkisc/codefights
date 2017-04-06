def areFollowingPatterns(strings, patterns):

    # keep k/v pairs in a dictionary
    # 
    # go through strings, patterns simultaneously and check:
        # if string[i] not in dict
            # add string[i] and pattern[i] to dict as a k/v pair
        # if string[i] in dict and pattern[i] does not match
            # return False
    # return True
    
    myMap = {}
    myOtherMap = {}
    
    x = len(strings)
    
    for i in range(0,x):
        if strings[i] not in myMap:
            myMap[strings[i]] = patterns[i]
        else:
            if myMap[strings[i]] != patterns[i]:
                return False
            
        if patterns[i] not in myOtherMap:
            myOtherMap[patterns[i]] = strings[i]
        else:
            if myOtherMap[patterns[i]] != strings[i]:
                return False            
        
    return True


#Note: Write a solution with O(n2) time complexity, 
#since this is what you would be asked to do during a #real interview.

#You have an array a composed of exactly n elements. 
#Given a number x, determine whether or not a contains 
#three elements for which the sum is exactly x.

import itertools
def tripletSum(x, a):

    m = list( itertools.combinations(a, 3) )
    
    for item in m:
        if sum(item) == x:
            return True
        
    return False

#You have two integer arrays, a and b, and an integer target value v. 
#Determine whether there is a pair of numbers, 
#where one number is taken from a and the other from b, that can be added together to get a sum of v. 
#Return true if such a pair exists, otherwise return false.

def sumOfTwo(a, b, v):
    for num in a:
        if v-num in b:
            return True
    return False


#You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
#Try to solve this in-place - in a real interview, you will only be allowed to use O(1) additional memory.

def rotateImage(a):
    
    # given an index, returns column entries (at that index) in a list
    def column(i):
        lst = []
        x = len(a)-1
        while x > -1:
            lst.append(a[x][i])
        
            x -= 1
        
        return lst
        
    return [ column(i) for i in range(0,len(a)) ]

#An infinite number of boxes are arranged in a row and numbered from left to right. 
#The first box on the left is number 1, the next box is number 2, etc. n balls are 
#placed in n of the boxes, and there can only be one ball per box. 
#You want to organize the balls, so you decide to arrange all the balls next to each other. 
#They should occupy a contiguous set of boxes. You can take one ball and move it into an empty box in one move.

#Given an array balls that indicates the numbers of the boxes in which the balls are placed, find the minimum number of moves needed to organize the balls.

def ballsRearranging(balls):
        
    def fix(num):
        count = 0
        start = num
        zeroes = [0 for i in range(0,len(balls))]
        for ball in balls:
            i = 0
            while i < len(balls):
                if (start+i) not in balls:
                    zeroes[count] += 1

                i += 1

            count += 1
            start -= 1

        return min(zeroes)
    
    return min([fix(num) for num in balls])


#Given two words, beginWord and endWord, and a wordList of approved words, 
#find the length of the shortest transformation sequence from beginWord to endWord such that:

#Only one letter can be changed at a time
#Each transformed word must exist in the wordList.
#Return the length of the shortest transformation sequence, or 0 if no such transformation sequence exists.

#Note: beginWord does not count as a transformed word. You can assume that beginWord and endWord 
#are not empty and are not the same.

import copy

def wordLadder(beginWord, endWord, wordList):
    
    def generateWordList(beginWord, wList):
        lst = []
        for word in wList:
            if oneAway(beginWord, word):
                lst.append(word)
        return lst
    
    # returns True if word1 and word2 are exactly one letter change apart
    # it's assumed that len(word1) == len(word2)
    def oneAway(word1, word2):
        i = 0
        count = 0
        while i < len(word1):
            if word1[i] != word2[i]:
                count += 1
            i += 1
        return count == 1
    
    def climbLadder(beginWord, endWord, wList, num):
        if beginWord == endWord:
            return num 
        
        # generate the word list
        # return min( [ climbLadder(BW, endWord, wordList, num+1) for BW in generated word list ] )
        WL = copy.deepcopy(wList)
        if beginWord in WL:
            WL.remove(beginWord)
        words = generateWordList(beginWord, WL)
        if words == []:
            return 99 # hmm...
        return min( [ climbLadder(BW, endWord, WL, num+1) for BW in words ] )
        
        
    # return generateWordList('hit')
    # print(oneAway('hit', 'dit'))    
    
    answer = climbLadder(beginWord, endWord, wordList, 1)
    
    if answer == 99:
        return 0
    return answer


#Given a rectangular matrix, return all of the elements of the matrix in spiral order.

def matrixElementsInSpiralOrder(matrix):
    
    def collectRight():
        for num in matrix.pop(0):
            nums.append(num)
        
    def collectDown():
        i = 0
        x = len(matrix[0])-1
        while i < len(matrix):
            nums.append(matrix[i][x])
            matrix[i].pop(x)
            i += 1
        
    def collectLeft():
        for num in reversed( matrix.pop(len(matrix)-1) ):
            nums.append(num)
            
    def collectUp():
        i = len(matrix)-1
        while i > -1:
            nums.append(matrix[i][0])
            matrix[i].pop(0)
            i -= 1
    
    def collect():
        direction = "right"
        
        while matrix != []:
            
            if direction == "right":
                collectRight()
                direction = "down"   
            elif direction == "down":
                collectDown()
                direction = "left"
            elif direction == "left":
                collectLeft()
                direction = "up"
            elif direction == "up":
                collectUp()
                direction = "right"
        
    nums = []
    collect()
    return nums


#You have an array nums. We determine two functions to perform on nums. 
#In both cases, n is the length of nums:

#fi(nums) = nums[0] · nums[1] · ... · nums[i - 1] · nums[i + 1] · ... · nums[n - 1]. 
#(In other words, fi(nums) is the product of all array elements except the ith f.)

#g(nums) = f0(nums) + f1(nums) + ... + fn-1(nums).

#Using these two functions, calculate all values of f modulo the given m. 
#Take these new values and add them together to get g. 
#You should return the value of g modulo the given m.

def productExceptSelf(nums, m):

    def multiply():
        mult = nums[0]
        i = 1
        x = len(nums)
        while i < x:
            mult *= nums[i]
            i += 1
        return mult
    
    mult = multiply()
    
    return ( sum([(mult//nums[i])%m for i in range(0,len(nums))]) )%m