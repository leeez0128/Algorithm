import sys
input = sys.stdin.readline


def solution(n):
    end = 2*n + 1
    prime = [True] * end
    count = 0
    for i in range(2, int(end**0.5)+1):
        if prime[i]:
            for j in range(i+i, end, i):
                prime[j] = False

    for i in range(n+1, end):
        if i > 1 and prime[i]:
            count += 1
    print(count)


# 베르트랑 공준
if __name__ == '__main__':
    while True:
        n = int(input().strip())
        if n == 0:
            break
        solution(n)
