"""
1456. Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""
def maxVowels(self, s: str, k: int) -> int:
    count = 0
    max_count = 0
    size = 0
    vowel = "aeiou"
    for i in range(len(s)):
        if s[i] in vowel:
            count+=1
            max_count = max(count,max_count)
        size+=1
        if size==k and s[i-(k-1)] in vowel:
            count -=1
            size -=1
        elif size == k and s[i-(k-1)] not in vowel:
            size -=1
    return max_count
