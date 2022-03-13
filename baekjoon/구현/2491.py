import sys
input = sys.stdin.readline


def solution(N, seq):
    increase_length = 1
    increase_temp = 1
    for i in range(1, N):
        if seq[i-1] <= seq[i]:
            increase_temp += 1
            increase_length = max(increase_length, increase_temp)
        else:
            increase_temp = 1

    decrease_length = 1
    decrease_temp = 1
    for i in range(1, N):
        if seq[i-1] >= seq[i]:
            decrease_temp += 1
            decrease_length = max(decrease_length, decrease_temp)
        else:
            decrease_temp = 1
            
    print(max(increase_length, decrease_length))


if __name__ == '__main__':
    N = int(input().strip())
    seq = list(map(int,input().strip().split()))
    solution(N, seq)
