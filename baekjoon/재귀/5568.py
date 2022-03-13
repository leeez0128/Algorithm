import sys
from itertools import permutations
input = sys.stdin.readline

def solution(k, card):
    number = []
    number_list = list(permutations(card, k))
    for _set in number_list:
        num = ''
        for idx in range(len(_set)):
            num += _set[idx]
        if num not in number:
            number.append(num)
    
    print(len(number))


if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    card = []
    for _ in range(n):
        card.append(input().strip())
    solution(k, card)    