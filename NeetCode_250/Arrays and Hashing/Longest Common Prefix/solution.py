class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        shortestString = min(strs, key=len) # saves the shortest string
        m = len(shortestString) # gets the length of the shortest string
        n = len(strs) # gets the length of strs
        longestPrefix = ""

        # iterates through each index of the shortest string
        for i in range(m):

            # iterates through each string in strs, excluding the shortest string
            for j in range(n):

                currentWord = strs[j]

                # don't want to include the shortestString in the sequence search
                if currentWord != shortestString:

                    # if the sequence breaks
                    if currentWord[i] != shortestString[i]:
                        return longestPrefix

            longestPrefix += shortestString[i] # adds the current index of shortestString to the sequence

        return longestPrefix