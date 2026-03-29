class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # define right, left
        right = len(nums)-1
        left = 0
        
        while left <= right:
            # find middle index
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # moving left to mid+1 if condition true    
            elif nums[mid] < target:
                left = mid + 1
            
            # moving right to mid-1 if condition true
            else:
                right = mid - 1
                
        return -1   
            
            

        
        
        

        