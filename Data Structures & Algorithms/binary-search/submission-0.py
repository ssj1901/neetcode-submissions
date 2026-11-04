class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            if nums[0] == target:
                return 0
            else:
                return -1
        l,r=0,len(nums)
        while l<r:
            half = int((l+r)/2)
            if(nums[half]==target):
                return half
            elif l==half or r==half:
                return -1
            elif (nums[half]>target):
                r=half
            else:
                l=half
        return -1
        
        