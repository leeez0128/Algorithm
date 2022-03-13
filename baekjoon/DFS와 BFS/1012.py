import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def search(col, row, graph):
    if row < 0 or row >= M or col < 0 or col >= N:
        return
    
    if graph[col][row] == 1:
        graph[col][row] = 0
        search(col+1, row, graph)
        search(col-1, row, graph)
        search(col, row+1, graph)
        search(col, row-1, graph)
    else:
        return


def solution(M, N, K, graph):
    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                search(i, j, graph)
                answer += 1
                
    print(answer)
                

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        M, N, K = map(int, input().strip().split())
        graph = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            X, Y = map(int, input().strip().split())
            graph[Y][X] = 1
        
        solution(M, N, K, graph)
        