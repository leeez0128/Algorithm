# 순열 라이브러리 사용 
# import sys
# from itertools import permutations
# input = sys.stdin.readline


# def solution(N, M):
#     arr = [i for i in range(1, N+1)]
#     seq = list(permutations(arr, M))
#     for i in range(len(seq)):
#         for j in range(len(seq[i])):
#             print(seq[i][j], end=" ")
#         print()


# if __name__ == '__main__':
#     N, M = map(int, input().strip().split())
#     solution(N, M)


# 백트래킹- 스택 구현
import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline
result = []


def DFS(N, M):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(1, N+1):
        if i in result:
            continue
        else:
            result.append(i)
            DFS(N, M)
            result.pop()
            print('what : ', *result)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    DFS(N, M)
