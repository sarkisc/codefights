


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


#ARRAYS
#

#Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

def firstNotRepeatingCharacter(s):
    
    nonRepeating = []
    repeating = []
    i = 0
    x = len(s)
    while i < x:
        if s[i] in nonRepeating:
            nonRepeating.remove(s[i])
            repeating.append(s[i])
            i += 1
        elif s[i] in repeating:
            i += 1
        else:
            nonRepeating.append(s[i])
            i += 1
    
    if nonRepeating == []:
        return "_"
    else:
        return nonRepeating[0]


#You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

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

#HASH TABLES
#

#You have a list of dishes. Each dish is associated with a list of ingredients used to prepare it. You want to group the dishes by ingredients, 
#so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).
#Return an array where each element is a list with the first element equal to the name of the ingredient and all of the other elements equal to the names of dishes that contain this ingredient. 
#The dishes inside each list should be sorted lexicographically. The result array should be sorted lexicographically by the names of the ingredients in its elements.

def groupingDishes(dishes):
    
    ingredients = {} # ingredient (string) --> list of dishes (list)
    ingredientCount = {} # ingredient (string) --> count (int)
    
    for dish in dishes:
        for i in range(1, len(dish)):
            if dish[i] not in ingredients.keys():    
                ingredients[dish[i]] = [dish[0]]
            else:
                ingredients[dish[i]] += [dish[0]]
            if dish[i] not in ingredientCount.keys():    
                ingredientCount[dish[i]] = 1
            else:
                ingredientCount[dish[i]] += 1
                
    ans = sorted([[ingr] for ingr in ingredients.keys() if ingredientCount[ingr] > 1])
    
    for i in range(len(ans)):
        ans[i] += sorted(ingredients[ans[i][0]])

    return ans


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


#Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

def containsCloseNums(nums, k):
    
    numMap = {} # num (int) --> list of indices (list)
    
    for i in range(len(nums)):
        if nums[i] not in numMap.keys():
            numMap[nums[i]] = [i]
        else:
            for num in numMap[nums[i]]:
                if i - num <= k:
                    return True
            numMap[nums[i]] += [i]
    return False


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


#Given a linked list l, reverse its nodes k at a time and return the modified list. 
#k is a positive integer that is less than or equal to the length of l. 
#If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.


def reverseNodesInKGroups(l, k):
    
    Groups = [] # list of pointers to linked list groups
    reverseFinalGroup = False
    nodeCount = 0
    curNode = l
    
    while curNode is not None:
        if nodeCount % k == 0:
            Groups.append(curNode)
        tempNode = curNode
        curNode = curNode.next
        if (nodeCount+1) % k == 0:
            tempNode.next = None
        nodeCount += 1
    if nodeCount % k == 0:
        reverseFinalGroup = True
        
    # now reverse each group
    for i in range(len(Groups)-1):
        Groups[i] = reverseLinkedList(Groups[i])
    if reverseFinalGroup:
        Groups[-1] = reverseLinkedList(Groups[-1])
    for i in range(len(Groups)-1):
        getLastNode(Groups[i]).next = Groups[i+1]
    l = Groups[0]
    return l
        

# reverses a linked list, returns it
def reverseLinkedList(l):
    links = []
    curNode = l
    while curNode is not None:
        tempNode = curNode
        curNode = curNode.next
        tempNode.next = None
        links = [tempNode] + links
    for i in range(len(links)):
        if i+1 in range(len(links)):
            links[i].next = links[i+1]
    l = links[0]
    return l

# returns the final link in a linked list
def getLastNode(l):
    curNode = l
    while curNode.next is not None:
        curNode = curNode.next
    return curNode


#Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.
#Try to solve this task in O(list size) time using O(1) additional space.

def rearrangeLastN(l, n):
    # keep two pointers pointing at nodes in linked lists
    # pointer further along in linked list is n ahead of first pointer
    # 
    # say l = [1, 2, 3, 4, 5] and n = 3
    # 
    # we reach a point where...
    # we have trailer pointing at node with value 2 (call this node s)
    # we have leader pointing at node with value 5 (call this node t)
    # 
    # save value for s.next (call this v; this will be the new start node)
    # s.next = null
    # t.next = l
    # return v
    
    if l is None or n == 0:
        return l
    
    trailer = leader = l
    for i in range(n):
        leader = leader.next
        if leader == None:
            return l
    
    while leader.next is not None:
        trailer = trailer.next
        leader = leader.next
    
    ans = trailer.next
    trailer.next = None
    leader.next = l
    return ans


#TREES (BASIC)
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


#Consider a special family of Engineers and Doctors. This family has the following rules:

#Everybody has two children.
#The first child of an Engineer is an Engineer and the second child is a Doctor.
#The first child of a Doctor is a Doctor and the second child is an Engineer.
#All generations of Doctors and Engineers start with an Engineer.

#Given the level and position of a person in the ancestor tree above, find the profession of the person.
#Note: in this tree first child is considered as left child, second - as right.

def findProfession(level, pos):
    
    # level-1 tells you how many bits to keep
    # pos-1 tells you what the bits are
    
    strPos = str(bin(pos-1)[2:])
    while len(strPos) < (level-1):
        strPos = '0' + strPos
        
    curProf = 'Engineer'
    for bit in strPos:
        if curProf == 'Engineer' and bit == '1':
            curProf = 'Doctor'
        elif curProf == 'Doctor' and bit == '1':
            curProf = 'Engineer'
    
    return curProf


#A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and the right subtrees must also be binary search trees.

#Given a binary search tree t, find the kth smallest element in it.
#Note that kth smallest element means kth element in increasing order.

def kthSmallestInBST(t, k):
    # inorder traversal
    # helper would help...
    return inorder(t, [k, t.value])[1]

    
# takes in t, [k, v], returns [k, v]
def inorder(t, kv):
    
    if kv[0] == 0:
        return kv
    if (t.left == None) and (t.right == None):
        return [kv[0]-1, t.value]
    
    # check left 
    leftSearch = None   
    if t.left is not None:
        leftSearch = inorder(t.left, [kv[0], t.value])
        if leftSearch[0] == 0:
            return leftSearch
    
    # check yourself
    meSearch = None
    if leftSearch is not None:
        meSearch = [leftSearch[0]-1, t.value]
    else:
        meSearch = [kv[0]-1, t.value]
    if (meSearch[0] == 0) or (t.right is None):
        return meSearch
    
    # check right
    return inorder(t.right, meSearch)


#Given two binary trees t1 and t2, determine whether the second tree is a subtree of the first tree. 
#A subtree for vertex v in a binary tree t is a tree consisting of v and all its descendants in t. 
#Determine whether or not there is a vertex v (possibly none) in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2.

def isSubtree(t1, t2):
    
    if t1 is None:
        if t2 is None:
            return True
        return False

    if equalTrees(t1, t2):
        return True
    else:
        return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)
    
# returns True if t1 and t2 are the same tree
# returns False otherwise
def equalTrees(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is not None and t2 is not None:
        if t1.value == t2.value:
            return (equalTrees(t1.left, t2.left) and equalTrees(t1.right, t2.right))
    return False
            

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


#Given a 2D grid skyMap composed of '1's (clouds) and '0's (clear sky), count the number of clouds. 
#A cloud is surrounded by clear sky, and is formed by connecting adjacent clouds horizontally or vertically. 
#You can assume that all four edges of the skyMap are surrounded by clear sky.

def countClouds(skyMap):
    
    if skyMap == []:
        return 0
    
    count = 0
    
    visited = []
    for i in range(len(skyMap)):
        v = [[False]*len(skyMap[0])]
        visited += v
    
    for i in range(len(skyMap)):
        for j in range(len(skyMap[0])):
            if visited[i][j] == False and skyMap[i][j] == '1':
                DFS(i, j, visited, skyMap)
                count += 1
    return count
                

def DFS(i, j, visited, skyMap):
    
    visited[i][j] = True
    # left
    if (j-1) in range(len(visited[0])) and visited[i][j-1] == False and skyMap[i][j-1] == '1':
        DFS(i, j-1, visited, skyMap)
    # right
    if (j+1) in range(len(visited[0])) and visited[i][j+1] == False and skyMap[i][j+1] == '1':
        DFS(i, j+1, visited, skyMap)
    # down
    if (i+1) in range(len(visited)) and visited[i+1][j] == False and skyMap[i+1][j] == '1':
        DFS(i+1, j, visited, skyMap)
    # up
    if (i-1) in range(len(visited)) and visited[i-1][j] == False and skyMap[i-1][j] == '1':
        DFS(i-1, j, visited, skyMap)


#TREES (ADVANCED)
#

#A tree height can be calculated as the length of the longest path in it (it is also called tree diameter).
#Find the tree diameter.

def treeDiameter(n, tree):
    
    # get the max depth of the tree from the root (it could be any node, really)
    # then take a node at max depth from the root and find the max depth from that node
    # return the latter
    
    if tree == []:
        return 0
    
    adjacentNodes = {} # node (int) -> list of adjacent nodes (list)
    for item in tree:
        n1, n2 = item[0], item[1]
        if n1 in adjacentNodes:
            adjacentNodes[n1].append(n2)
        else:
            adjacentNodes[n1] = [n2]
        if n2 in adjacentNodes:
            adjacentNodes[n2].append(n1)
        else:
            adjacentNodes[n2] = [n1]
    
    startNode = tree[0][0]
    lst1 = BFS(startNode, adjacentNodes, 0, n)
    
    return BFS(lst1[0], adjacentNodes, 0, n)[1]

    
# returns a list of two elements: [someNodeAtMaxDepth, maxDepth]
def BFS(startNode, adjacentNodes, depth, n):
    
    visited = set()
    visited.add(startNode)
    queue = [[startNode, depth]]
    
    while len(visited) < n:
        item = queue.pop(0)
        for node in adjacentNodes[item[0]]:
            if node not in visited:
                queue.append([node,item[1]+1])
                visited.add(node)
    
    return max(queue, key=lambda item: item[1])


#The sum of a subtree is the sum of all the node values in that subtree, including its root.
#Given a binary tree of integers, find the most frequent sum (or sums) of its subtrees.

def mostFrequentSum(t):
    
    if t is None:
        return []

    sumMap = {} # sum (int) -> numOccurrences (int)
    getSum(t, sumMap)
    
    maxOccurrences = max(sumMap.values())
    return sorted([key for key in sumMap.keys() if (sumMap[key] == maxOccurrences)])
    
    
def getSum(t, sumMap):
    
    leftSum = rightSum = 0
    
    if t.left is not None:
        leftSum = getSum(t.left, sumMap)
             
    if t.right is not None:
        rightSum = getSum(t.right, sumMap)
        
    val = t.value + leftSum + rightSum
    
    if val in sumMap:
        sumMap[val] += 1
    else:
        sumMap[val] = 1
        
    return val


#GRAPHS
#

#We will represent the nodes by integers 0, ...., n - 1. We represent the adjacent edges using a two-dimensional list, connections. 
#If j is in the list connections[i], then there is a directed edge from node i to node j.

#Write a function that returns True if connections describes a graph with a directed cycle, or False otherwise.

def hasDeadlock(connections):
    # run search alg, keeping track of which nodes have been visited...
    # if you come across start node again, you're done

    visited = set()
    for i in range(len(connections)):
        visited.add(i)
        nodeSearch = DFCS(connections, i, visited)
        if nodeSearch:
            return True
        visited = set()
    return False
    
# returns True if cycle found; False otherwise
def DFCS(connections, startNode, vSet):
    for node in connections[startNode]:
        if node in vSet:
            return True
        else:
            vSet.add(node)
            nodeSearch = DFCS(connections, node, vSet)
            if nodeSearch:
                return True
            vSet.remove(node)
    return False
        

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



#DP (BASIC)
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


#You are planning to rob houses on a specific street, and you know that every house on the street has a certain amount of money hidden. 
#The only thing stopping you from robbing all of them in one night is that adjacent houses on the street have a connected security system. 
#The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.
#Given a list of non-negative integers nums representing the amount of money hidden in each house, determine the maximum amount of money you can rob in one night without triggering an alarm.

def houseRobber(nums):
    # take the max of everything other than the last one
    # then add that to the current
    
    if nums == []:
        return 0
    
    l = [0]*len(nums)
    l[0] = mxAmt = nums[0]
    for i in range(1, len(nums)):
        maxAmount = nums[i]
        for j in range(0, i-1):
            curAmount = l[j] + nums[i]
            if curAmount > maxAmount:
                maxAmount = curAmount
        l[i] = maxAmount
        if maxAmount > mxAmt:
            mxAmt = maxAmount

    return mxAmt


#Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

def composeRanges(nums):
    
    ranges = []
    
    i = 0
    while i < len(nums):
        startNum = endNum = nums[i]
        while (i+1) < len(nums) and nums[i+1] == nums[i] + 1:
            endNum += 1
            i += 1
        
        ranges.append(getRange(startNum, endNum))
        
        i += 1
        
    return ranges
        

        
def getRange(startNum, endNum):
    if startNum == endNum:
        return str(startNum)
    else:
        return str(startNum) + "->" + str(endNum)


#DP (ADVANCED)
#

#You have a 2D binary matrix that's filled with 0s and 1s. In the matrix, find the largest square that contains only 1s and return its area.

def maximalSquare(matrix):
    
    if len(matrix) == 0:
        return 0
    
    mtx = [[int(item) for item in matrix[0]]]
    
    maxNum = max(mtx[0], key=lambda item: int(item))
    
    for i in range(1,len(matrix)):
        num = int(matrix[i][0])
        if num > maxNum:
            maxNum = num
        mtx.append([num])
        for j in range(1,len(mtx[0])):
            if matrix[i][j] == '0':
                mtx[i].append(0)
            elif matrix[i][j] == '1':
                num = min(mtx[i-1][j-1], mtx[i][j-1], mtx[i-1][j]) + 1
                mtx[i].append(num)
                if num > maxNum:
                    maxNum = num

    return maxNum**2


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


#Given an integer n, replace its bits starting from the bit at position a to the bit at position b, inclusive, 
#with the bits of integer k. Count from the least significant bit to the most significant bit, starting from 0.

def insertBits(n, a, b, k):
    
    binN = bin(n)[2:]
    binK = bin(k)[2:]
    
    while len(binN) < (b+1):
        binN = '0' + binN
        
    while len(binK) < (b-a+1):
        binK = '0' + binK

    if a != 0:
        return int(binN[:-(b+1)] + binK + binN[-a:], 2)
    return int(binN[:-(b+1)] + binK, 2)





#COMMON TECHNIQUES (ADVANCED)
#

#All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T. In research, it can be useful to identify repeated sequences within DNA.
#Write a function to find all the 10-letter sequences (substrings) that occur more than once in a DNA molecule s, and return them in lexicographical order. These sequences can overlap.

def repeatedDNASequences(s):
    
    if len(s) < 10:
        return []
    
    tenLetterSequences = set()
    TLS_appearMoreThanOnce = set()
    
    for i in range(0,len(s)-9):
        tenLetrSeq = s[i:i+10]
        if tenLetrSeq in tenLetterSequences:
            TLS_appearMoreThanOnce.add(tenLetrSeq)
        else:
            tenLetterSequences.add(tenLetrSeq)
            
    return sorted(list(TLS_appearMoreThanOnce))


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


#A rational number is the ratio of two integers, where the denominator is not zero. We are going to represent the rational number numerator / denominator as the ordered pair (numerator, denominator).

#There are many different tuples representing the same rational number. 
#For instance, one-half is (1, 2), (2, 4), (3, 6), etc. 
#Your task is to write a function that, given the numbers numerator and denominator representing the ratio numerator / denominator, returns an array [a, b] of two integers where:

#(a, b) represents the same rational number as (numerator, denominator) but in simplified format;
#a and b have no non-trivial factors;
#b is positive.

def simplifyRational(numerator, denominator):

    # deal with negatives...
    numNegatives = 0
    if numerator < 0:
        numNegatives += 1
        numerator *= -1
    if denominator < 0:
        numNegatives += 1
        denominator *= -1
    
    x = gcd(numerator, denominator)
    
    while x > 1:
        numerator, denominator = numerator/x, denominator/x
        x = gcd(numerator, denominator)

    # bring negatives back if necessary...
    if numNegatives % 2 == 1:
        numerator *= -1
        
    return [numerator, denominator]


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


#You're having a big party and you're serving a pizza as a main dish. You got really tired of cutting the pizza, so you decided to do it as efficiently as possible by using no more than n cuts.
#Each cut is required to be a straight line, and there is no requirement that the pizza pieces be the same size.
#Given n, the number of straight cuts you're willing to make, find the maximum number of pieces you can cut the pizza into.

def lazyCutter(n):
    return n*(n+1)/2 + 1