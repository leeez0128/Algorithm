import sys
input = sys.stdin.readline


def solution(numbers):
    multiResult = str(numbers[0] * numbers[1] * numbers[2])
    answer = [0 for _ in range(10)]
    for i in range(len(multiResult)):
        answer[int(multiResult[i])] = answer[int(multiResult[i])] + 1
    
    
    for i in range(len(answer)):
        print(answer[i])



if __name__ == '__main__':
    numbers = [int(input().strip()) for _ in range(3)]
    solution(numbers)