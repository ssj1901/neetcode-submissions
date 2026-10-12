class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set={""}
        prev_length=len(new_set)
        for num in nums:
            new_set.add(num)
            length=len(new_set)
            if length == prev_length:
                return True
            else:
                prev_length=length
        return False
        