import sys
input = sys.stdin.readline

# 시간 초과
# def solution(N, seqA):
#     for i in range(N):
#         for j in range(i+1, N):
#             if seqA[i] < seqA[j]:
#                 print(seqA[j], end=" ")
#                 break
#         else:
#             print("-1", end=" ")

# stack
def solution(N, seqA):
    NGE = [-1] * N
    stack = []
    
    for i in range(N):
        while stack and seqA[stack[-1]] < seqA[i]:
            NGE[stack.pop()] = seqA[i]
        stack.append(i)
    
    print(*NGE)


if __name__ == '__main__':
    N = int(input().strip())
    seqA = list(map(int, input().strip().split()))
    solution(N, seqA)
