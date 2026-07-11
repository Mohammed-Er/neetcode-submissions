class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        left = 0
        right = left + 1
        for i in range(len(nums) - 1):
            if nums[left] == nums[right]:
                return True
            left += 1
            right += 1
        
        return False