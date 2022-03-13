import sys
input = sys.stdin.readline


def solution(word):
    answer = []
    for first_section in range(1, len(word)-2):
        for second_section in range(first_section+1, len(word)):
            first = word[:first_section][::-1]
            second = word[first_section:second_section][::-1]
            third = word[second_section:][::-1]
            answer.append(first + second + third)
    answer.sort()
    print(answer[0])


if __name__ == '__main__':
    word = input().strip()
    solution(word)
