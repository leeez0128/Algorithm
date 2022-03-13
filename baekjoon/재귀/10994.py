import sys
input = sys.stdin.readline


def solution(N):
    for i in range(N-1):
        print("* "*i, "*"*(1 + 4*(N-i-1)), " *"*i, sep="")    
        print("* "*(i+1), " "*(1 + 4*(N-i-2)), " *"*(i+1), sep="")
    print("* "*(2*N - 1))
    for i in range(N-1):
        print("* "*(N - i - 1), " "*(1 + 4*i), " *"*(N - i - 1), sep="")
        print("* "*(N - i - 2), "*"*(1 + 4*(i+1)), " *"*(N - i - 2), sep="")


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
