import sys
input = sys.stdin.readline


def solution(N):
    if len(N) == 1:
        N = '0'+ N

    cycle = N
    count = 0

    while True:
        second = str(int(cycle[0]) + int(cycle[1]))
        if(len(second)==2):
            second = second[1]
    
        cycle = cycle[1] + second 
        # print('cycle: ', cycle)
        count = count + 1

        if(N == cycle):
            break

    print(count)


if __name__ == '__main__':
    N = input().strip()
    solution(N)
