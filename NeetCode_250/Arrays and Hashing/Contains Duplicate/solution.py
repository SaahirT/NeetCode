class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # get length of nums
        n = len(nums)

        # error condition
        if(n < 2):
            return False

        # make a hashset
        mySet = set()

        for i in range (n):
            if nums[i] not in mySet:
                mySet.add(nums[i])
            else:
                return True

        return False
