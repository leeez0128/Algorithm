import sys
input = sys.stdin.readline


def solution(N):
    count = 0
    for i in range(len(N)-1):
        count += 9 * 10**i * (i+1)
    
    print(count + (int(N) - 10**(len(N)-1) + 1)*len(N))


if __name__ == '__main__':
    N = input().strip()
    solution(N)
