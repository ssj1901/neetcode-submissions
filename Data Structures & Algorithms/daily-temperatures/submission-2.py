class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack=[]
        for i,num in enumerate(temperatures):
            while stack and stack[-1][1]<num:
                stackInd,stackNum=stack.pop()
                res[stackInd]= i - stackInd
            stack.append((i,num))
        return res