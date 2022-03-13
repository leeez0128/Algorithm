import sys
input = sys.stdin.readline


def solution(testcase):
    for case in testcase:
        average = (sum(case) - case[0]) / case[0]
        up = 0
        for i in range(1, case[0]+1):   
            if case[i] > average:
                up += 1
        print("{:.3f}%".format(up/case[0]*100))
        

if __name__ == '__main__':
    C = int(input().strip())
    testcase = []
    for _ in range(C):
        testcase.append(list(map(int, input().strip().split())))
    solution(testcase)
