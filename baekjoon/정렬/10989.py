import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    result = [0] * 10001
    for _ in range(N):
        result[int(input().strip())] += 1
    for i in range(len(result)):
        for _ in range(result[i]):
            print(i)
