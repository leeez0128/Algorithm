import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

binary = []

def toBinary(N):
    if N // 2 == 1:
        result = '1' + str(N % 2)
        return result
    
    binary.append(N % 2)
    return toBinary(N//2)


if __name__ == '__main__':
    N = int(input().strip())
    binary.append(toBinary(N))
    for num in reversed(binary):
        print(num, end="")
