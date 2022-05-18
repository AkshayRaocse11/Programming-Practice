#https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for i in range(0,len(strs[0])):           
            for s in strs:
                if i == len(s) or s[i]!=strs[0][i]:
                    return result
            result +=  strs[0][i]
                
        return result
                    
                
        
        
                