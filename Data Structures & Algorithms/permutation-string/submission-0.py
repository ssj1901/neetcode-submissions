class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=[0]*26
        count=[0]*26
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            need[ord(s1[i])-ord('a')]+=1
            count[ord(s2[i])-ord('a')]+=1
        if count==need:
            return True
        for r in range(len(s1),len(s2)):
            count[ord(s2[r-len(s1)])-ord('a')]-=1
            count[ord(s2[r])-ord('a')]+=1
            if count == need:
                return True          
        return False