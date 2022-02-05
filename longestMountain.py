class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0 
        up = 1
        down = 0
        n = len(arr)
        for i in range(1, n):
            if arr[i] > arr[i-1] and down == 0:
                up += 1
            elif arr[i] < arr[i-1] and up > 1:
                down += 1
            else:
                if up > 1 and down:
                    res = max(res, up + down)
                up = 2 if arr[i] > arr[i - 1] else 1
                down = 0
        if up and down:
            res = max(res, up + down)
        return res
                
            
        
