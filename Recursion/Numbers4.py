'''print N to 1 using Backtracking'''

def Numbers(i, n):
    if i < 1:
        return
    Numbers(i - 1, n)
    print(n - i + 1)
if __name__ == "__main__":
    n = int(input())
    Numbers(n, n)