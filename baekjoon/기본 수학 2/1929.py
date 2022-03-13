import sys
input = sys.stdin.readline


# 에라토스테네스의 체
# 배수들을 제거하여 소수만 남긴다 
def solution(M, N):
    N += 1
    prime = [True] * N
    for i in range(2, int(N**0.5)+1):
        if prime[i]:
            for j in range(i+i, N, i):
               prime[j] = False
    
    for i in range(M, N):
        if i > 1 and prime[i]:
            print(i)
        

if __name__ == '__main__':
    M, N = map(int, input().strip().split())
    solution(M, N)
