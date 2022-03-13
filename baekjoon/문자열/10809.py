import sys
input = sys.stdin.readline


def solution(S):
    result = [-1 for _ in range(26)]
    for i in range(len(S)):
        alphabet = int(ord(S[i])) - 97
        if result[alphabet] == -1:
            result[alphabet] = i

    for ele in result:
        print(ele, end=" ")


if __name__ == '__main__':
    S = input().strip()
    solution(S)
