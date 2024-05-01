"""You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array."""

"""Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations."""

def maxOperations(self, nums: List[int], k: int) -> int:
        #find the two pairs
        count = 0
        # Sort the list to use two pointers approach
        nums.sort()
        # Initialize two pointers
        left, right = 0, len(nums) - 1
        
        while left < right:
            # Calculate the sum of current pair
            curr_sum = nums[left] + nums[right]
            if curr_sum == k:
                # If sum equals k, increment count and move both pointers
                count += 1
                left += 1
                right -= 1
            elif curr_sum < k:
                # If sum is less than k, move left pointer to the right
                left += 1
            else:
                # If sum is greater than k, move right pointer to the left
                right -= 1
        
        return count
