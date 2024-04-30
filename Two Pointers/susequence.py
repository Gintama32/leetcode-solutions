"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not)."""
"""Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false"""

def isSubsequence(self, s: str, t: str) -> bool:
        #take a first pointer, set it to char of s
        sp = 0
        #take second pointer to search for thh char of s in first pointer
        tp = 0
        while sp<len(s):
            while tp<len(t) and t[tp] != s[sp]:
                    tp+=1
            if tp == len(t):
                return False
        # move it until not equal
        #if not found return False
        # once found move the first pointer, move the second pointer by 1 to ensure the order is maintained 
            sp +=1
            tp+=1
        return True
