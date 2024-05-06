"""
1493. Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
"""
def longestSubarray(self, nums: List[int]) -> int:
    l,r = 0,0
    k=1
    c=0
    max_c =0 
    while r<len(nums):
        if nums[r]==0:
            k-=1
        if k<0:
            if nums[l]==0:
                k+=1
            l+=1
        c = r-l
        max_c = max(max_c,c)
        r+=1
    return max_c