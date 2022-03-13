import sys
input = sys.stdin.readline


def solution(n):
    selfnumber = []
    for i in range(10):
        selfnumber.append(i + i)

    for i in range(10, 100):
        selfnumber.append(i + int(str(i)[0]) + int(str(i)[1]))

    for i in range(100, 1000):
        selfnumber.append(i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]))

    for i in range(1000, 10000):
        selfnumber.append(i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]))
    
    for i in range(10000):
        if i not in selfnumber:
            print(i)


if __name__ == '__main__':
    solution(10000)
