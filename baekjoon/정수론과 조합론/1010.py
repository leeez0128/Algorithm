import sys, math
input = sys.stdin.readline


def solution(left, right):
    print(math.factorial(right) // (math.factorial(left) * math.factorial(right-left)))


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        left, right = map(int, input().strip().split())
        solution(left, right)
