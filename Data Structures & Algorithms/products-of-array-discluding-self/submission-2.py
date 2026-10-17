class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        p = None
        zero_cnt = 0

        for num in nums:
            if p is None:
                p = num
            elif num != 0:
                p = p * num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return [0] * len(nums)

        for i in range(len(nums)):
        
            if nums[i] != 0:
                if not zero_cnt:
                    res.append(p//nums[i])
                else:
                    res.append(0)
            else:
                res.append(p)

        return res
        