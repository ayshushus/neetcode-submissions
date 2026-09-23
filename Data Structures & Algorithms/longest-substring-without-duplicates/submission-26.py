class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        dict = {}
        for r in range(len(s)):
            
            if s[r] in dict:
                l = max(l, dict[s[r]] + 1)
            
            dict[s[r]] = r
            length = max(length,r - l + 1)

        return length
            











"""
        length = 0
        maxLength = 0
        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                maxLength = max(maxLength, length)
                length = i - seen[s[i]]
                # take the old i from the s[i] so far and update length to the difference bw current i and that old i and update i to newer index
                seen[s[i]] = i
                continue
            length += 1
            seen[s[i]] = i
        return length
"""
