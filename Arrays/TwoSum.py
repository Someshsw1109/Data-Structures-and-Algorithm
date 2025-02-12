class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hashmap = {} #Empty hashmap
        for i, num in enumerate(nums): #Traverse the array
            complement = target - num
            if complement in Hashmap:
                return [Hashmap[complement], i]
            Hashmap[num] = i
        return []
solution = Solution()
nums = list(map(int, input().split()))
target = int(input())
res = solution.twoSum(nums, target)
print(res)
