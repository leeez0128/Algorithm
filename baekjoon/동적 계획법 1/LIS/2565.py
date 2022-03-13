#전깃줄
import sys
input = sys.stdin.readline


def solution(N, elect):
    longest_up = [1 for _ in range(N)]
    for i in range(1, N):
        for j in range(i):
            if elect[j][1] < elect[i][1]:
                longest_up[i] = max(longest_up[i], longest_up[j]+1)

    print(N - max(longest_up))


if __name__ == '__main__':
    N = int(input().strip())
    elect = []
    for _ in range(N):
        A, B = map(int, input().strip().split())
        elect.append((A, B))
    elect.sort()
    solution(N, elect)
