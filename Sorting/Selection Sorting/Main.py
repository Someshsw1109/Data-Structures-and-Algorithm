'''
Selectionn Sorting --> Pick the minimum element from the list and place it to the first position.

'''

class Solution:
    def SelectionSort(self, arr, n):
        for i in range(0, n - 2):
            Mini = i
            for j in range(i, n - 1):
                if arr[j] < arr[Mini]:
                    Mini = j
            Temp = arr[Mini]
            arr[Mini] = arr[i]
            arr[i] = Temp
solution = Solution()
n = int(input())
arr = list(map(int, input().split()))
res = solution.SelectionSort(arr, n)
# print(res)
print(arr)

# Time complexity - O(n**2)
# This is the best, worst and average time complexity for this particular algorithm....
