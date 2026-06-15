class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # Sort to easily skip duplicates
        
        def backtrack(current, used):
            if len(current) == len(nums):
                res.append(list(current))
                return
            
            for i in range(len(nums)):
                # Skip if already used in current path
                if used[i]:
                    continue
                
                # Skip if it's a duplicate of the previous element and 
                # the previous element hasn't been used in this path.
                # This ensures only the first instance of a duplicate 
                # is used for a specific position in the permutation.
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                current.append(nums[i])
                backtrack(current, used)
                
                # Backtrack
                used[i] = False
                current.pop()
        
        backtrack([], [False] * len(nums))
        return res
