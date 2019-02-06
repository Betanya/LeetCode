"""
Code by Bethany Roberts 
last edited: 2/6/2019

includes deep analysis of code
"""

"""
nums represents an array of numbers
target represents the sum of two numbers in the array

the purpose of the code is to iterate through the array until the addition of two numbers in the array are equal to the target.
the two indices must be unique. 
"""
class Solution(object):
  def twoSum(self, nums, target):
    """
    enumerate function is used to find the value(numValueOne & Two) and index(indexOne & Two) of the element. 
    
    enumerate function passes through two values through the array, indexOne or Two being the counter.
    nums is the array in use. 0 is the number that the counter will be starting at. 
    since Python starts indices at 0, the counter was initialized at 0. 
    """
    
    for indexOne, numValueOne in enumerate(nums, 0):
        #print("for loop one")
        #print(indexOne, numValueOne)
        
        """
        everytime the first for loop goes through once and generates the index and produes the value,
        the second for loop goes through it's entire array. 
        
        eg. loopOne= 0 loopTwo= 0,1,2,3
        
        this means every possible value will be found. 
        how? because eventually the first loop will loop through all of it's numbers and when it does, the second for loop is checking 
        every possible value against each number in the first for loop.
        
        eg. if you had a room full of speed daters. Lexi, Bev, and Liza with Tom, Brad, and Steve. 
        the speed dating game is such that everyone has a number. If any of the ladies (eg.the first for loop) numbers 
        add up to "the number of love" with one of the guys, they win an all inclusive date.
        
        So Lexi (index 0, loop 1) addes her number with Tom (index 0), Brad (index 1), and Steve (index 2). None of them match.
        Bev (index 1, loop 1) does the same and she matches with Steve! They win a date.
        
        """
        
        for indexTwo, numValueTwo in enumerate(nums, 0): 
            #print("for loop two")
            #print(indexTwo, numValueTwo)
            
            """
            So if "Lexi + Steve = "number of love" then they win.
            But wait, Lexi and Steve can't be in the same place in line. They aren't they are good.
            But Lexi and Tom can't date because they are both in first place in the line-up(darn)(eg. index 0)
            
            """
            if numValueOne + numValueTwo == target and indexOne != indexTwo:
                #print(indexTwo, indexOne)
                #print(numValueOne, numValueTwo, target)
                
                """
                once the conditions are met, the dating game ends because there is only one "number of love". 
                The names of the winners are announced. 
                
                """
                #return acts as a break function and ends the program once the condition is met. 
                
                return indexTwo, indexOne
                
            
