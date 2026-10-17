class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # dictionary to store the mapping of values
        nums_mapping_idx = {}

        for i, x in enumerate(nums):
            nums_mapping_idx[x] = i

        for i, x in enumerate(nums):
            diff = target-x
            if diff in nums_mapping_idx and i != nums_mapping_idx.get(diff):
                return sorted([i, nums_mapping_idx[diff]])
        return []