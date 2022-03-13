import sys
input = sys.stdin.readline


def solution(A):
  A = sorted(A)
  print(A[-3])


if __name__ == '__main__':
  T = int(input().strip())
  for _ in range(T):
    solution(list(map(int, input().strip().split())))
