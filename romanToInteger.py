"""
Code by Bethany Roberts
Last edited on 2/9/2019
"""

"""
The purpose of this code is to convert a string of roman numerals into their numeric values.
"""



class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #convert the str into an array to iterate through it.
        #the [] indicate it will be an array.
        #str(val) selects the individual value for each interation through the string,
        #and causes there to be commas seperating the individual value from the rest. 
        #anything placed int eh "str(val)" position will then be separated by commas. 
        strArray =[str(val) for val in str(s)]
        
  
        #set values of the what the int of the roman numerals will be. 
        #set value for the condition checking index, which will be 1 greater than the actual index.
        intVal = 0
        iCheck = 0
        
        #add the correct amount for every roman numeral as 
        #it iterates through the string.
        
        #if I, X, or C is before V & X
        #L & C, D & M,
        #Then it is 4 and 9, 40 and 90, 400 and 900
        
        for i, romN in enumerate(strArray, 0):
            
            #iCheck is the index before i so we can see if the I is before X or V ect.
            iCheck = i + 1
            
            #Checking conditions are met for IV and IX
            if iCheck < len(strArray) and strArray[i] == 'I' and strArray[iCheck] == 'V':
                intVal -= 2
                print intVal
            if iCheck < len(strArray) and strArray[i] == 'I' and strArray[iCheck] == 'X':
                intVal -= 2
                print intVal
            
            #Check conditions are met for XL and XC.
            #less than sign because indices are the actual position minus one.
            if iCheck < len(strArray) and strArray[i] == 'X' and strArray[iCheck] == 'L':
                intVal -= 20
                print intVal
            if iCheck < len(strArray) and strArray[i] == 'X' and strArray[iCheck] == 'C':
                intVal -= 20
                print intVal
            #Check conditions are met for CD and CM.
            print len(strArray) 
            print iCheck
            if iCheck < len(strArray) and strArray[i] == 'C' and strArray[iCheck] == 'D':
                intVal -= 200
                print intVal
            if iCheck < len(strArray) and strArray[i] == 'C' and strArray[iCheck] == 'M':
                intVal -= 200
                print intVal    
            
            #must use if statements instead of elif, because these values must be assigned even after the condition is met.    
            if romN == 'I':
                intVal += 1
            if romN == 'V':
                intVal += 5
            if romN == 'X':
                intVal += 10
            if romN == 'L':
                intVal += 50
            if romN == 'C':
                intVal += 100
            if romN == 'D':
                intVal += 500
            if romN == 'M':
                intVal += 1000
                
        return intVal
