class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        triedMap = {} # Store index and value of previously tested elements

        for i, n in enumerate(nums):
            diff = target - n
            if diff in triedMap:
                return [triedMap[diff], i]
            triedMap[n] = i
        return