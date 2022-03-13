import sys
input = sys.stdin.readline


def solution(A, B, m, A_nums):
    ten_num = 0
    for num in range(m):
        ten_num += (A ** num) * A_nums[m-num-1]

    result = []
    while ten_num:
        if ten_num < B:
            result.append(ten_num)
            break
        result.append(ten_num % B)
        ten_num //= B
    
    for i in range(len(result)-1, -1, -1):
        print(result[i], end=" ")


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    m = int(input().strip())
    A_nums = list(map(int, input().strip().split()))
    solution(A, B, m, A_nums)
