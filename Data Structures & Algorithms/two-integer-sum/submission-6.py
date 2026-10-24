class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev=defaultdict()
        for i,num in enumerate(nums):
            diff=target-num
            if diff in prev.keys():
                return [prev[diff],i]
            else:
                prev[num]=i
        return []