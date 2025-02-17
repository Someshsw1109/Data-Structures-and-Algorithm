'''Print Name N times using recursion'''

def Name(i, n):
    if i > n:
        return
    print("Somesh")
    Name(i + 1, n)
if __name__ == "__main__":
    n = int(input())
    Name(1, n)
    