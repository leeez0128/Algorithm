import sys
input = sys.stdin.readline


def solution(alphabet):
    set_alphabet = set(alphabet)
    sorted_alphabet = sorted(set_alphabet, key=lambda x:(len(x),x))
    for word in sorted_alphabet:
        print(word)


if __name__ == '__main__':
    N = int(input().strip())
    alphabet = []
    for _ in range(N):
        alphabet.append(input().strip())
    solution(alphabet)
