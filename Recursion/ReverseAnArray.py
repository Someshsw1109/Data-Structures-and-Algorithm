# def Arr(arr):
#     return arr[::-1]
# if __name__ == "__main__":
#     arr = list(map(int, input().split()))
#     print(Arr(arr))

from typing import List

class Solution:
    def ReverseAnArray(self, i: int, arr: List[int], n: int)->List[int]:
        if i >= n // 2:
            return
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        self.ReverseAnArray(i + 1, arr, n)
        return arr
solution = Solution()
n = int(input())
arr = list(map(int, input().split()))
res = solution.ReverseAnArray(0, arr, n)
print(res)
