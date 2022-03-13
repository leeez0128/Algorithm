import sys
input = sys.stdin.readline


def solution(A, B):
    common = [[0] * (len(B)+1) for _ in range(len(A)+1)]

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                common[i][j] = common[i-1][j-1] + 1
            else:
                common[i][j] = max(common[i-1][j], common[i][j-1])
    
    print(common[-1][-1])


if __name__ == '__main__':
    A = input().strip()
    B = input().strip()
    solution(A, B)
