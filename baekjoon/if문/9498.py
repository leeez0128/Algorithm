import sys
input = sys.stdin.readline


def solution(score):
    if(90 <= score <= 100):
        print("A")
    elif(80 <= score <= 89):
        print("B")
    elif(70 <= score <= 79):
        print("C")
    elif(60 <= score <= 69):
        print("D")
    else:
        print("F")


if __name__ == '__main__':
    score = int(input().strip())
    solution(score)
