##Problem 1
# two sum

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        # print(num)
        residue = target - num
        if residue in seen:
            return [i, seen[residue]]

        seen[num] = i
    return []

print(twoSum([2,7,11,9],9))
