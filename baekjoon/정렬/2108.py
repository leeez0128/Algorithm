import sys
from collections import Counter
input = sys.stdin.readline


def solution(numbers):
    print(round(sum(numbers)/len(numbers))) # 산술평균 
    
    numbers.sort()
    print(numbers[len(numbers)//2]) # 중앙값
    

    frequency = Counter(numbers).most_common()
    if len(frequency) > 1 and frequency[0][1] == frequency[1][1]:
        print(frequency[1][0]) # 최빈값
    else:
        print(frequency[0][0])

    print(max(numbers) - min(numbers)) # 범위


if __name__ == '__main__':
    N = int(input().strip())
    numbers = [int(input().strip()) for _ in range(N)]
    solution(numbers)
