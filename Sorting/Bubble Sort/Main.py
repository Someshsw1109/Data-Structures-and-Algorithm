'''
Bubble Sort --> Pick the maximum element and place it to the last position.

'''


class Solution:
    def BubbleSort(self, arr, n):
        for i in range(n - 1, 0, -1):
            for j in range(0, i):
                if arr[j] > arr[j + 1]:
                    Temp = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = Temp
        return arr

solution = Solution()
n = int(input())
arr = list(map(int, input().split()))
res = solution.BubbleSort(arr, n)
print(res)
# print(arr)
