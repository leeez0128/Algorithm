import sys
input = sys.stdin.readline

# 탐색에서 큰 메모리 문제가 발생하는 경우라면? '이분탐색'
def solution(N, k):
    start = 1
    end = N*N
    while(start <= end):
        mid = (start + end) // 2
        cnt = 0
        for i in range(1, N+1):
            cnt += min(mid//i, N)
        
        if cnt >= k:
            end = mid - 1
        else:
            start = mid + 1
    
    print(start)
    

if __name__ == '__main__':
    N = int(input().strip())
    k = int(input().strip())
    solution(N, k)
