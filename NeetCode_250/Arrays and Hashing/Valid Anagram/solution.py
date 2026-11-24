class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # sort both strings in alphabetical order, then check if they are equal
        if sorted(s) == sorted(t):
            return True
        else:
            return False