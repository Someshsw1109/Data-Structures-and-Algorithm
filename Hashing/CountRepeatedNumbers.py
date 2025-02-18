# Count the number of repeated integers in an array

from typing import List

# Brute Force 
class Solution:
    def CountRepeated(self, arr: List[int], n: int) -> int:
        count = 0
        for i in range(len(arr)):
            if arr[i] == n:
                count += 1
        return count
solution = Solution()
arr = list(map(int, input().split()))
n = int(input())
res = solution.CountRepeated(arr, n)
print(res)
