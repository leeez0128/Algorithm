import sys
input = sys.stdin.readline


def solution(N):
    zero_to_ten = [0 for _ in range(9)]

    for num in N:
        if num == '9':
            zero_to_ten[6] += 1
        else:
            zero_to_ten[int(num)] += 1
    
    if zero_to_ten[6] % 2 == 0:
        zero_to_ten[6] //= 2
    else:
        zero_to_ten[6] = zero_to_ten[6] // 2 + 1
    
    print(max(zero_to_ten))


if __name__ == '__main__':
    N = input().strip()
    solution(N)
