class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target= len(nums)-1
        index=target-1
        
        while(index!=-1 and target!=0):
            print(nums[index],index,target)
            if(nums[index]+index>=target):
                target=index
                index-=1
            else:
                index-=1
        if target==0 and index==-1:
            return 1
        return 0
