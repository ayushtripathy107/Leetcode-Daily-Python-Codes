class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :type rtype: int
        """
        n = len(arr)
        memo = {}

        def dp(i):
            # If already computed, return the cached result
            if i in memo:
                return memo[i]
            
            max_visited = 1  # You can always at least visit the starting index
            
            # 1. Jump to the right: i + x
            for x in range(1, d + 1):
                j = i + x
                if j >= n: 
                    break
                if arr[j] >= arr[i]: 
                    break  # Blocked by a taller or equal bar
                max_visited = max(max_visited, 1 + dp(j))
                
            # 2. Jump to the left: i - x
            for x in range(1, d + 1):
                j = i - x
                if j < 0: 
                    break
                if arr[j] >= arr[i]: 
                    break  # Blocked by a taller or equal bar
                max_visited = max(max_visited, 1 + dp(j))
                
            memo[i] = max_visited
            return max_visited

        # Find the maximum possible indices visited starting from any position
        return max(dp(i) for i in range(n))
