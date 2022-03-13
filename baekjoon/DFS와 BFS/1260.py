import sys
from collections import deque
input = sys.stdin.readline


def DFS(N, M, V, graph, visited):
    print(V, end=" ")
    visited[V] = True
    
    for node in graph[V]:
        if not visited[node]:
            DFS(N, M, node, graph, visited)    


def BFS(N, M, V, graph):   
    visited = [False] * (N+1)
    visited[V] = True
    
    queue = deque([V])
    while queue:
        poped_edge = queue.popleft()
        print(poped_edge, end=" ")
        for node in graph[poped_edge]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
    
    
def solution(N, M, V, graph):
    visited = [False] * (N+1)
    
    for i in range(1, N+1):
        graph[i].sort()
        
    DFS(N, M, V, graph, visited)
    print()
    BFS(N, M, V, graph)


if __name__ == '__main__':
    N, M, V = map(int, input().strip().split())
    graph = [[] for _ in range(N+1)]
    # 양방향 
    for _ in range(M):
        start, end = map(int, input().strip().split())
        graph[start].append(end)
        graph[end].append(start)
    solution(N, M, V, graph)