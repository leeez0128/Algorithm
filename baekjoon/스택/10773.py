import sys
input = sys.stdin.readline


if __name__ == '__main__':
    K = int(input().strip())
    result = []
    for _ in range(K):
        num = int(input().strip())
        if num == 0:
            result.pop()
        else:
            result.append(num)
            
    print(sum(result))
