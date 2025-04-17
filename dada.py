from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        for string in strs[1:]:
            # Check and shorten the prefix until it matches the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:  # If prefix becomes empty
                    return ""
        
        return prefix

# Example usage
solution = Solution()
strings = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strings))  # Output: "fl"