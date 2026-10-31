class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        res=''
        l=0
        
        for r in range(len(s)):
            while s[r] in s[l:r]:
                l+=1

            if len(s[l:r+1]) > len(res):
                res= s[l:r+1]            
            
        return len(res)
