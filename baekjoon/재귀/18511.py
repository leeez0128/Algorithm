from itertools import product
import sys
input = sys.stdin.readline


def solution(N, list_K):
    len_N = len(str(N))
    numbers = []
    while True:
        numbers = list(product(list_K, repeat=len_N))
        result = []
        for nums in numbers:
            number = int(''.join(nums))
            if number <= N:
                result.append(number)
                
        if len(result) >= 1:
            print(max(result))
            break
        else:
            len_N -= 1


if __name__ == '__main__':
    N, _ = map(int, input().strip().split())
    list_K = list(map(str, input().strip().split()))
    solution(N, list_K)
