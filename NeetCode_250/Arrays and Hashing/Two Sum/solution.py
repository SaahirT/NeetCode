class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # get length of nums
        n = len(nums)

        for i in range(n):
            difference = target - nums[i]

            try: 
                j = nums.index(difference, i+1)
                return [i, j]

            except ValueError:
                pass