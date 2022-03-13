import sys
input = sys.stdin.readline


def solution(seq):
    result = 0
    for word in seq:
        group = dict()
        for i in range(len(word)):
            if word[i] not in list(group.keys()):
                group[word[i]] = i
            else:
                if group[word[i]] == i-1:
                    group[word[i]] = i
                else:
                    break
            if i == (len(word) -1):
                result += 1
                break
    
    print(result)


if __name__ == '__main__':
    N = int(input().strip())
    seq = [input().strip() for _ in range(N)]
    solution(seq)
