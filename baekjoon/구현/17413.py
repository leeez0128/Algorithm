import sys
input = sys.stdin.readline


def reverse_(tag, word):
    tags = tag.split(" ")
    for arr in tags:
        word += arr[::-1]
        word += " "
    return word


def solution(S):
    tag = ''
    word = ''
    for i in range(len(S)):
        if S[i] == '<':
            if tag == "":
                tag += S[i]
                continue
            word = reverse_(tag, word).rstrip()
            tag = ''
            tag += S[i]
        elif S[i] == '>':
            tag += S[i]
            word += tag
            tag = ''

        else:
            tag += S[i]
        
        if i == len(S)-1:
            word = reverse_(tag, word)

    print(word)


if __name__ == '__main__':
    S = input().strip()
    solution(S)
