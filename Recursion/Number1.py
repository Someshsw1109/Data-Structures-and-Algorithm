'''print 1 to N using recursion'''

def Numbers(i, n):
    if i > n:
        return
    print(i)
    Numbers(i + 1, n)
if __name__ == "__main__":
    n = int(input())
    Numbers(1, n)