'''
Merge Sort --> Divide and Merge

'''

class Solution:
    def Merge(self, arr, low, mid, high):
        left = low
        right = mid + 1
        NewArray = []
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                NewArray.append(arr[left])
                left += 1
            else:
                NewArray.append(arr[right])
                right += 1
        while left <= mid:
            NewArray.append(arr[left])
            left += 1
        while right <= high:
            NewArray.append(arr[right])
            right += 1
        
        for i in range(low, high + 1):
            arr[i] =  NewArray[i - low]

    def mergeSort(self, arr, low, high):
        if low == high:
            return
        if low < high:
            mid = (low + high) // 2
            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid + 1, high)
            self.Merge(arr, low, mid, high)
    def MergeSort(self, arr, n):
        self.mergeSort(arr, 0, n - 1)
        return arr
    # def MergeSort(self, arr, n):
        # Write Your Code here
        
        # pass

solution = Solution()
n = int(input())
arr = list(map(int, input().split()))
res = solution.MergeSort(arr, n)
print(res)