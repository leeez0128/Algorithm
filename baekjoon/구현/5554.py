import sys
input = sys.stdin.readline

if __name__ == '__main__':
    answer = 0
    for _ in range(4):
        answer += int(input().strip())
    print(answer//60)
    print(answer%60)