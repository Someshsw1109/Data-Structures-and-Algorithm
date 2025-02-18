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


# Using Hashing

class Somesh:
    def CountRepeated1(self, arr: List[int], q: int) -> int:
        n = max(arr) + 1
        HashCounts = [0] * n
        for i in range(n):
            HashCounts[arr[i]] += 1
        while q:
            number = int(input())
            print(HashCounts[number])
            q -= 1
somesh = Somesh()
arr = list(map(int, input().split()))
q = int(input())
res = somesh.CountRepeated1(arr, q)
print(res)
