import sys
input = sys.stdin.readline


def solution(A, B):
    if(A > B):
        print(">")
    elif(A < B):
        print("<")
    elif(A == B):
        print("==")


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    solution(A, B)
