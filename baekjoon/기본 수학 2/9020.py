import sys
input = sys.stdin.readline


def solution(even):
    orgin = even
    even += 1
    prime = [True] * even
    for i in range(2, int(even**0.5)+1):
        if prime[i]:
            for j in range(i+i, even, i):
                prime[j] = False
    
    for i in range(orgin//2, 1, -1):
        if prime[i] and prime[orgin-i]:
            print(i, orgin-i)
            break


# 골드바흐의 추측
# 10000보다 작거나 같은 모두 짝수 n에 대한 골드바흐 파티션은 존재
if __name__ == '__main__':
    T = int(input().strip())
    even = [int(input().strip()) for _ in range(T)]
    for even_num in even:
        solution(even_num)
