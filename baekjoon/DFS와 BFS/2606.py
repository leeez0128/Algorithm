from collections import deque
import sys
input = sys.stdin.readline


def solution(N, M, graph):
    visited = [False] * (N+1)
    visited[1] = True
    
    queue = deque([1])
    answer = 0
    while queue:
        poped_edge = queue.popleft()
        for node in graph[poped_edge]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                answer += 1
    print(answer)


if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())
    graph = [[] for _ in range(N+1)]
    # 양방향 
    for _ in range(M):
        start, end = map(int, input().strip().split())
        graph[start].append(end)
        graph[end].append(start)
    solution(N, M, graph)
