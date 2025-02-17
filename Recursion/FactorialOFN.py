'''Function Recursion'''

def Factorial(n: int)->int:
    if n == 0:
        return 1
    return n * Factorial(n - 1)
if __name__ == "__main__":
    n = int(input())
    print(Factorial(n))


'''Parameterized Recursion'''
def Factorial(i, F):
    if i < 1:
        print(F)
        return
    Factorial(i - 1, F*i)
if __name__ == "__main__":
    n = int(input())
    Factorial(n, 1)
