'''Sum of N Numbers using Recursion'''

'''Code - 1'''
# def SumOfNumbers(i, n):
#     if i > n:
#         return 0
#     return i + SumOfNumbers(i + 1, n)
# if __name__ == "__main__":
#     n = int(input())
#     print(SumOfNumbers(1, n))

'''Code - 2'''
# def Sum(i, S):
#     if i < 1:
#         print(S)
#         return
#     Sum(i - 1, S + i)
# if __name__ == "__main__":
#     n = int(input())
#     Sum(n, 0)

'''Code - 3'''

def Sum(n: int)->int:
    if n == 0:
        return 0
    return n + Sum(n - 1)
if __name__ == "__main__":
    n = int(input())
    print(Sum(n))
# All the above codes are for Sum of N numbers using Recursion

