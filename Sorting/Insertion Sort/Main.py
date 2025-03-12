'''
Insertion sort --> Take an element and place it in its correct orders

'''

class Solution:
    def InsertionSort(self, arr, n):
        for i in range(1, n):
            j = i
            while j > 0 and arr[j - 1] > arr[j]:
                # arr[j - 1], arr[j] = arr[j], arr[j - 1] --> we can also swap using this line of code.
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
                j -= 1
        return arr
    
solution = Solution()
n = int(input())
arr = list(map(int, input().split()))
res = solution.InsertionSort(arr, n)
print(res)

# Time complexity --> For Worst and Average case it will be O(N**2) and for best case it will be O(N) 
# In best case code will runs only one for loop because there is no swaps happened so while loop will not runs.