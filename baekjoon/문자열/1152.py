import sys
input = sys.stdin.readline


def solution(sentence):
    return len(sentence)


if __name__ == '__main__':
    sentence = input().strip().split()
    print(solution(sentence))
