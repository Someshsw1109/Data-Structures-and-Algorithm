'''Print 1 to N using Backtracking'''

def Numbers(i, n):
    if i < 1:
        return
    Numbers(i - 1, n)
    print(i)
if __name__ == "__main__":
    n = int(input())
    Numbers(n, n)