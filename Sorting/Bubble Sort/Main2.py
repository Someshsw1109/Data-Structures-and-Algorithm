'''
Optimised Code for Bubble Sort

'''

class Solution:
    def BubbleSort(self, arr, n):
        for i in range(n - 1, 0, -1):
            SwapDone = 0
            for j in range(0, i):
                if arr[j] > arr[j + 1]:
                    Temp = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = Temp
                    SwapDone = 1
            if SwapDone == 0:
                break
            # print("runs\n")
        return arr

solution = Solution()
n = int(input())
arr = list(map(int, input().split()))
res = solution.BubbleSort(arr, n)
print(res)


'''This code runs in O(n) time in best case and o(n**2) in worst and average case'''