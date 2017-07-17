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


#HASH TABLES
#
#Given an array strings, determine whether it follows the sequence given in the patterns array. 
#In other words, there should be no i and j for which 
#strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

def areFollowingPatterns(strings, patterns):
    
    match1 = {} # String (from strings) -> String (from patterns)
    match2 = {} # String (from patterns) -> String (from strings)
    
    for i in range(len(strings)):
        curString1 = strings[i]
        curString2 = patterns[i]
        
        if curString1 in match1 and curString2 in match2:
            if not (match1[curString1] == curString2 and match2[curString2] == curString1):
                return False

        elif (curString1 in match1 and not curString2 in match2) or (curString2 in match2 and not curString1 in match1):
            return False
        else:
            match1[curString1] = curString2
            match2[curString2] = curString1
            
    return True


# LINKED LISTS
#
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

#Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

def removeKFromList(l, k):
    
    if l == None:
        return l
    
    while l.value == k:
        l = l.next
        if l == None:
            return l
    
    curNode = l
    
    while curNode.next != None:
        if curNode.next.value == k:
            curNode.next = curNode.next.next
        else:
            curNode = curNode.next
            
    return l


#Given a singly linked list of integers, determine whether or not it's a palindrome.

def isListPalindrome(l):
    curNode = l
    a = []
    while curNode != None:
        a.append(curNode.value)
        curNode = curNode.next
    
    return a == a[::-1]



#You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. 
#The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

def addTwoHugeNumbers(a, b):
    # extract the numbers
    # add them to get their sum
    # put this sum in a linked list, in the desired format
    # problem: carry
    # 
    # load the links' values into arrays
    # zero out the beginning elems of the array of lesser length until both arrays are of the same length
    # create a new array
    # have an extra element at the start, value set to zero
    # add the numbers into the new array
    # each array element gets sum of corresponding element values and carry, mod 10000
    # carry gets updated with sum div 10000
    
    arr = None
    arrA = linkedListToArray(a)
    arrB = linkedListToArray(b)
    
    if len(arrA) != len(arrB):
        if len(arrA) < len(arrB):
            arr = arrA
        else:
            arr = arrB
    while len(arrA) != len(arrB):
        arr.insert(0, 0)
    
    arr = [0]*(len(arrA)+1)
    carry = 0
    i = len(arrA)-1
    while i > -1:
        arr[i+1] = (arrA[i] + arrB[i] + carry)%10000
        carry = (arrA[i] + arrB[i] + carry)//10000
        i -= 1
    arr[0] += carry
    if arr[0] == 0:
        arr.pop(0)
        
    return arrayToLinkedList(arr)
    
    
def linkedListToArray(lnkLst):
    arr = []
    curNode = lnkLst
    while curNode != None:
        arr.append(curNode.value)
        curNode = curNode.next
    return arr

def arrayToLinkedList(arr):
    lnkLst = None
    if len(arr) == 0:
        return lnkLst
    lnkLst = ListNode(arr[0])
    curNode = lnkLst
    for i in range(1, len(arr)):
        curNode.next = ListNode(arr[i])
        curNode = curNode.next
    return lnkLst


#Given two singly linked lists sorted in non-decreasing order, your task is to merge them. 
#In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

def mergeTwoLinkedLists(l1, l2):
    
    if l1 == None:
        return copyLinkedList(l2)
    elif l2 == None:
        return copyLinkedList(l1)
    else:
        curNode1 = l1
        curNode2 = l2
        mergedList = None
        if curNode1.value < curNode2.value:
            mergedList = ListNode(curNode1.value)
            curNode1 = curNode1.next
        else:
            mergedList = ListNode(curNode2.value)
            curNode2 = curNode2.next
        mergedListTraverser = mergedList
        while curNode1 != None and curNode2 != None:
            if curNode1.value < curNode2.value:
                mergedListTraverser.next = ListNode(curNode1.value)
                mergedListTraverser = mergedListTraverser.next
                curNode1 = curNode1.next
            else:
                mergedListTraverser.next = ListNode(curNode2.value)
                mergedListTraverser = mergedListTraverser.next
                curNode2 = curNode2.next
        
        if curNode1 != None:
            mergedListTraverser.next = copyLinkedList(curNode1)
            
        elif curNode2 != None:
            mergedListTraverser.next = copyLinkedList(curNode2)

        return mergedList

def copyLinkedList(lnkLst):
    if lnkLst == None:
        return None
    lnkLstCpy = ListNode(lnkLst.value)
    lnkLstTraverser = lnkLst.next
    lnkLstCpyTraverser = lnkLstCpy
    while lnkLstTraverser != None:
        lnkLstCpyTraverser.next = ListNode(lnkLstTraverser.value)
        lnkLstTraverser = lnkLstTraverser.next
        lnkLstCpyTraverser = lnkLstCpyTraverser.next
    return lnkLstCpy


#TREES
#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

#Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

def hasPathWithGivenSum(t, s):
    
    if t == None:
        if s == 0:
            return True
        return False
    
    nums = []
    traverse(t, nums)
    
    return s in nums

    
def traverse(node, nums, valueSoFar=0):
    
    val = valueSoFar + node.value
    
    if node.left == None or node.right == None:
        nums.append(val)
    if node.left != None:
        traverse(node.left, nums, val)
    if node.right != None:
        traverse(node.right, nums, val)


#Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

def isTreeSymmetric(t):
    # do BFS
    # check if each level's values make a palindrome

    if t == None:
        return True
    
    queue = [t]
    levels = [0]
    curLevel = 0
    
    while queue != []:
        values = []
        while levels != [] and levels[0] == curLevel:
            curNode = queue.pop(0)
            if curNode != None:
                values.append(curNode.value)
                queue.append(curNode.left)
                levels.append(curLevel+1)
                queue.append(curNode.right)
                levels.append(curLevel+1)
            else:
                values.append(None)
            levels.pop(0)
        if values != values[::-1]:
            return False
        curLevel += 1
        
    return True
            

#HEAPS, STACKS, QUEUES
#

#Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

def kthLargestElement(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]


#Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....
#
#Here is some info on Unix file system paths:
#
#/ is the root directory; the path should always start with it even if it isn't there in the given path;
#/ is also used as a directory separator; for example, /code/fights denotes a fights subfolder in the code folder in the root directory;
#this also means that // stands for "change the current directory to the current directory"
#. is used to mark the current directory;
#.. is used to mark the parent directory; if the current directory is root already, .. does nothing.


def simplifyPath(path):
    parsedPath = path.split('/')
    
    #print(parsedPath)
    
    stack = []
    
    for item in parsedPath:
        if item == '..' or item == '.' or  item == '':
            if item == '..' and stack != []:
                stack = stack[:-1]
        else:
            stack.append(item)
    
    #print(stack)
    
    answer = '/'
    if stack != []:
        for item in stack:
            answer += item
            answer += '/'
        answer = answer[:-1]
    
    return answer



#Given an encoded string, return its corresponding decoded string.
#
#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

def decodeString(s):
    
    answer = ''
    
    i = 0
    while i in range(len(s)):
        if 96 < ord(s[i]) < 123:
            answer += s[i]
            i += 1
        elif 47 < ord(s[i]) < 58:
            
            repeatTimes = s[i]
            i += 1
            while 47 < ord(s[i]) < 58:
                repeatTimes += s[i]
                i += 1
                
            repeatTimes = int(repeatTimes)
            
            stg = ''
            numLeftSB = 0
            numRightSB = 0
            if s[i] == '[':
                numLeftSB += 1
            i += 1
            while numLeftSB > numRightSB:
                if s[i] == '[':
                    numLeftSB += 1
                elif s[i] == ']':
                    numRightSB += 1
                if numLeftSB > numRightSB:
                    stg += s[i]      
                i += 1               
            
            answer += decodeString(stg)*repeatTimes
            
    return answer
            

#Given an array a composed of distinct elements, find the next larger element for each element of the array, 
#i.e. the first element to the right that is greater than this element, in the order in which they appear in the array, and return the results as a new array of the same length. 
#If an element does not have a larger element to its right, put -1 in the appropriate cell of the result array.

def nextLarger(a):
    # create a stack and keep that stack's min and max
    # if you come across a number greater than the stack's max, great
    # else if you come across a number less than the stack's min, add the number to the stack
    # else (the number is less than the stack's max but greater than the stack's min)
        # go through the stack one number at a time, and establish a new min

    
    theAnswer = [-1]*len(a)
    theStack = [a[0]]
    theMin = a[0]
    theMax = a[0]
    curPlaceInArray = 0

    for i in range(1,len(a)):
        if a[i] > theMax:
            for j in range(curPlaceInArray, i):
                if theAnswer[j] == -1:
                    theAnswer[j] = a[i]
            curPlaceInArray = i
            theStack.append(a[i])
            theMax = a[i]
        elif a[i] < theMin:
            theStack.append(a[i])
            theMin = a[i]
        else:
            for j in range(curPlaceInArray, i):
                if (a[i] > theStack[j] and theAnswer[j] == -1):
                    theAnswer[j] = a[i]            
            theStack.append(a[i])
    return theAnswer


#Implement a modified stack that, in addition to using push and pop operations, allows you to find the current minimum element in the stack by using a min operation.

def minimumOnStack(operations):
    
    arr = []
    answer = []
    minSoFar = []
    theMin = float('inf')
    
    
    for op in operations:
        if op == 'min':
            answer.append(theMin)
        elif op[:4] == 'push':
            pshInt = int(op[5:])
            arr.append(pshInt)
            if pshInt < theMin:
                theMin = pshInt
                minSoFar.append(theMin)
            else:
                minSoFar.append(minSoFar[-1])
        elif op == 'pop':
            arr.pop()
            minSoFar.pop()
            if minSoFar != []:
                theMin = minSoFar[-1]
            else:
                theMin = float('inf')
            
            
    return answer
        

#DFS AND BFS
#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


#Given a binary tree of integers t, return its node values in the following format:

#The first element should be the value of the tree root;
#The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
#The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
#Etc.

def traverseTree(t):
    
    # while queue is not empty
        # get value
        # put its children in the queue
        # dequeue
    
    queue = [t]
    values = []
    
    while queue != []:
        curNode = queue.pop(0)
        if curNode != None:
            values.append(curNode.value)
            if curNode.left != None:
                queue.append(curNode.left)
            if curNode.right != None:
                queue.append(curNode.right)
        
    return values


#You have a binary tree t. Your task is to find the largest value in each row of this tree. 
#In a tree, a row is a set of nodes that have equal depth. For example, a row with depth 0 is a tree root, a row with depth 1 is composed of the root's children, etc.

#Return an array in which the first element is the largest value in the row with depth 0, the second element is the largest value in the row with depth 1, the third element is the largest element in the row with depth 2, etc.

def largestValuesInTreeRows(t):
    
    if t == None:
        return []
    
    queue = [t]
    maxes = []
    levels = [0]
    curLevel = 0
    
    while queue != []:
        values = []
        while levels != [] and levels[0] == curLevel:
            curNode = queue.pop(0)
            if curNode != None:
                values.append(curNode.value)
                if curNode.left != None:
                    queue.append(curNode.left)
                    levels.append(curLevel+1)
                if curNode.right != None:
                    queue.append(curNode.right)
                    levels.append(curLevel+1)
            levels.pop(0)
        maxes.append( max(values) )
        curLevel += 1
        
    return maxes
    

#We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

#Given a binary tree t, find the sum of all the numbers encoded in it. 
    
def digitTreeSum(t):
    
    # use DFS
    # use separate function
    
    nums = []
    traverse(t, nums)
    
    return sum(nums)

    
def traverse(node, nums, valueSoFar=0):
    
    val = 10*valueSoFar + node.value
    
    if node.left == None and node.right == None:
        nums.append(val)
    else: 
        if node.left != None:
            traverse(node.left, nums, val)
        if node.right != None:
            traverse(node.right, nums, val)
        
    
#SORTING
#
#ADD LATER!!!



#DP: BASIC
#
#DO MORE OF THESE!!!

#You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can climb to the top of the staircase.

def climbingStairs(n):
    
    # say n == 7
    # 1 1 1 1 1 1 1
    # 2 1 1 1 1 1
    # 2 2 1 1 1
    # 2 2 2 1
    
    fact = [1]
    i = 1
    while i < 51:
        fact.append(fact[i-1]*i)
        i += 1
    
    def nCr(n,r):
        return fact[n] / fact[r] / fact[n-r]
    
    count = 0
    i = 0
    num = n
    k = 0
    while i < (n//2)+1:
        
        count += nCr(num, k)
        num -= 1
        k += 1
        
        i += 1
    
    return count



#STRINGS
#

#You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

#Put a single space between the words.
#Convert the uppercase letters to lowercase.

def amendTheSentence(s):
    words = []
    curWord = ''
    for char in s:
        if 64 < ord(char) < 91:
            words.append(curWord)
            curWord = char
        else:
            curWord += char
    words.append(curWord)
    if '' in words:
        words.remove('')
    
    sentence = ""
    for i in range(len(words)):
        curWord = words[i]
        curWord += ' '
        curWord = decapitalize(curWord)
        sentence += curWord
    
    return sentence[:-1]
        


def decapitalize(word):
    firstChar = word[0]
    if 96 < ord(firstChar) < 123:
        return word
    firstChar = chr(ord(firstChar)+32)
    return firstChar + word[1:]



#BITS
#

#You are given an array of integers in which every element appears twice, except for one. 
#Find the element that only appears one time. Your solution should have a linear runtime complexity (O(n)). Try to implement it without using extra memory.

def singleNumber(nums):
    res = 0
    for num in nums:
        res = res ^ num
    return res


#NUMBER THEORY
#

#You are supposed to label a bunch of boxes with numbers from 0 to n, and all the labels are stored in the array arr. Unfortunately one of the labels is missing. Your task is to find it.

def missingNumber(arr):
    y = len(arr)
    x = set(range(0,y+1))
    
    i = 0
    while i < y:
        z = arr[i]
        if z in x:
            x.remove(z)
        
        i += 1
    
    return list(x)[0]