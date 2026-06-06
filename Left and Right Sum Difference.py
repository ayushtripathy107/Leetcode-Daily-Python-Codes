class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_sum = 0
        right_sum = sum(nums)
        answer = []
        
        for num in nums:
            # right_sum for the current index excludes the current number
            right_sum -= num
            
            # Calculate the absolute difference
            answer.append(abs(left_sum - right_sum))
            
            # Update left_sum to include the current number for the next index
            left_sum += num
            
        return answer
