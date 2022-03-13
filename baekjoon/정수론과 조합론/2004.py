import sys
input = sys.stdin.readline

# 시간 초과
# def solution(n, m):
#     num = str(math.factorial(n) // (math.factorial(n-m) * math.factorial(m)))
#     result = 0
#     for i in range(len(num)-1, -1, -1):
#         if int(num[i]) == 0:
#             result += 1
#         else:
#             print(result)
#             return

def divide_with(n, k):
    result = 0
    square = 1
    while True:
        num = n // (k**square)  #8! -> 8//2 8//2^2 8//2^3 ...
        result += num
        if num == 0:
            break
        square += 1
    return result


def solution(n, m):
    two = divide_with(n, 2) - divide_with(m, 2) - divide_with(n-m, 2)
    five = divide_with(n, 5) - divide_with(m, 5) - divide_with(n-m, 5)
    print(min(two, five))


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    solution(n, m)
