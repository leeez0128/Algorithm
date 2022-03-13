import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline


def solution(N):
    random = [0, 1, 2, 3]
    roma = [1, 5, 10, 50]
    result = []
    for num in combinations_with_replacement(random, N):
        hap = 0
        for i in num:
            hap += roma[i]
        result.append(hap)
        
    print(len(set(result)))
    
    
if __name__ == '__main__':
    N = int(input().strip())
    solution(N)