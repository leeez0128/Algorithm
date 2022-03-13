import sys
from enum import Enum
input = sys.stdin.readline


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


def RGBstreet(house):
    for i in range(1, len(house)):
        house[i][Color.RED.value] = min(house[i-1][Color.GREEN.value], house[i-1][Color.BLUE.value]) + house[i][Color.RED.value]
        house[i][Color.GREEN.value] = min(house[i-1][Color.RED.value], house[i-1][Color.BLUE.value]) + house[i][Color.GREEN.value]
        house[i][Color.BLUE.value] = min(house[i-1][Color.RED.value], house[i-1][Color.GREEN.value]) + house[i][Color.BLUE.value]

    print(min(house[len(house)-1][Color.RED.value] ,house[len(house)-1][Color.GREEN.value], house[len(house)-1][Color.BLUE.value]))


if __name__ == '__main__':
    N = int(input().strip())
    house = []
    for _ in range(N):
        house.append(list(map(int, input().strip().split())))
    
    RGBstreet(house)
