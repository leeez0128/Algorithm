import sys
input = sys.stdin.readline


def solution(N, A):
    longest_up = [1 for _ in range(N)]
    longest_down = [1 for _ in range(N)]
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                longest_up[i] = max(longest_up[i], longest_up[j]+1)
    
    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            if A[j] < A[i]:
                longest_down[i] = max(longest_down[i], longest_down[j]+1)

    answer = 0
    for i in range(N):
        if longest_up[i] + longest_down[i] > answer:
            answer = longest_up[i] + longest_down[i] - 1

    print(answer)
        

if __name__ == '__main__':
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    solution(N, A)
