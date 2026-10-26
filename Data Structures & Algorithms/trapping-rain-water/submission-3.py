class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        leftMax=height[l]
        rightMax=height[r]

        while l<r: 
            if leftMax<rightMax:
                res+=min(leftMax,rightMax)-height[l]
                l+=1
                leftMax=max(leftMax,height[l])
            else:
                res+=min(leftMax,rightMax)-height[r]
                r-=1
                rightMax=max(rightMax,height[r])
        return res    
            