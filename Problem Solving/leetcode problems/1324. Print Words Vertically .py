#https://leetcode.com/problems/print-words-vertically/
class Solution(object):
    def printVertically(self, s):
        words= s.split(" ")
        length = max(len(i) for i in words)
        
        result = []
        
        for i in range(length):  
            vertical = ""
            for word in words:
                vertical += word[i] if i<len(word) else " "
                
            vertical = vertical.rstrip()
            result.append(vertical)
            
        return result