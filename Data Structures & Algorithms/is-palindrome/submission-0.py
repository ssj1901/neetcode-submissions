class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=s.lower()
        i,j=0,len(s)-1
        while i<j:
            if not new_s[i].isalnum():
                print("Im in i")
                i+=1
                continue
            if not new_s[j].isalnum():
                print("Im in j")
                j-=1
                continue    
            if new_s[i]!=new_s[j]:
                print("Im in if block")
                return False
            i+=1
            j-=1
        return True