'''Print N to 1 using recursion'''

def Numbers(i, n):
    if i > n:
        return
    print(n - i + 1)
    Numbers(i + 1, n)
if __name__ == "__main__":
    n = int(input())
    Numbers(1, n)