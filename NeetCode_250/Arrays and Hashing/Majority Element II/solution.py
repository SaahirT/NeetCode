class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # convert the list into a set to only have the unique numbers
        # iterate through the set and get each element's count from the list
        # if the count > n/3 add it to the output, unless it's already in

        copied_nums = set(nums.copy())
        output = []
        for num in copied_nums:
            if nums.count(num) > (len(nums)/3): 
                output.append(num)
        return output