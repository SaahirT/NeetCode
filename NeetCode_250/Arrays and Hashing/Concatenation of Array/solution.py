class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # get the length of the nums array
        n = len(nums)

        # create the ans array with size 2n (fill with 0's for now)
        ans = [0] * 2 * n

        # iterate through nums twice
        for i in range(2 * n):
            ans[i] = nums[i - n]

        return ans