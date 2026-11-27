class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(len(nums)):
            current_min = min(nums)
            new_nums.append(current_min)
            nums.remove(current_min)
        return new_nums