class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Create an empty hashmap to store { value: index }
        seen = {}
        
        # 2. Loop through the list, getting both the index (i) and the number (n)
        for i, n in enumerate(nums):
            complement = target - n
            
            # 3. If the complement is already in our map, we found the pair!
            if complement in seen:
                return [seen[complement], i]
            
            # 4. Otherwise, store the current number and its index in the map
            seen[n] = i