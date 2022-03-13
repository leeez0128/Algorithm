# import sys
# input = sys.stdin.readline
# fibo = {0:0, 1:1}


# def solution(n):
#     if fibo.get(n) != None:
#         return fibo[n]
#     else:
#         if n % 2:
#             f = (solution((n+1)//2) % 1_000_000_007)**2 + (solution(n//2) % 1_000_000_007)**2
#         else:
#             f1 = solution(n//2 - 1) % 1_000_000_007
#             f2 = solution(n//2) % 1_000_000_007
#             f = ((f1 + f2) * f2 + f2 * f1) % 1_000_000_007
            
#         fibo[n] = f % 1_000_000_007
#         return f % 1_000_000_007


# if __name__ == '__main__':
#     n = int(input().strip())
#     print(solution(n))


import sys
input = sys.stdin.readline


def multiMatrix(matrix1, matrix2):
    result = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1_000_000_007
    return result
    
    
def solution(n):
    temp = [[1, 1], [1, 0]]
    result = [[0, 1], [1, 0]]
    while n:
        if n & 1:
            result = multiMatrix(temp, result)
        temp = multiMatrix(temp, temp)
        n //= 2
    
    print(result[0][0])


if __name__ == '__main__':
    n = int(input().strip())
    solution(n)