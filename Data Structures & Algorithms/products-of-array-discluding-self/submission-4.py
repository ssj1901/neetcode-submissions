class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        res, next = [1]*size, [1]*size
        i=0
        j=size-1
        while i < size:
            if i!=0:
                res[i]=res[i-1]*nums[i-1]
            i+=1
        while j >= 0:
            if j!=size-1:
                next[j]=nums[j+1]*next[j+1]
            j-=1
        i=0
        while i<size:
            res[i]=res[i]*next[i]
            i+=1
        return res