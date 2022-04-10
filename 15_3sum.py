class Solution:
    def threeSum(self, nums):
        def twoSum(nums, target):
            res = []
            for i in range(len(nums)):
                for j in range(i + 1, len(nums), 1):
                    if nums[i] + nums[j] == target:
                        if [nums[i], nums[j]] not in res and [nums[j], nums[i]] not in res:
                            res.append([nums[i], nums[j]])
            return res

        results = []
        for i, num in enumerate(nums):
            numc = nums
            target = 0 - num
            numc.pop(i)

            twopair = twoSum(numc, target)

            if len(twopair) > 0:
                for tp in twopair:
                    pairs = []
                    pairs.append(num)
                    pairs.extend(tp)
                    pairs.sort()
                    if pairs not in results:
                        results.append(pairs)

        return results
