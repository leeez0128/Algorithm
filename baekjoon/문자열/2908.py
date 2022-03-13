import sys
input = sys.stdin.readline


def solution(A, B):
    result = ''
    for i in range(2,-1, -1):
        if A[i] > B[i]:
            result = A[2] + A[1] + A[0]
            break
        elif A[i] < B[i]:
            result = B[2] + B[1] + B[0]
            break
        else:
            continue
    print(result)


if __name__ == '__main__':
    A, B = input().strip().split()
    solution(A, B)
