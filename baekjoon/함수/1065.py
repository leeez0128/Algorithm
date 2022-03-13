import sys
input = sys.stdin.readline

# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# 한자리수, 두자리수 : 무조건 한수

def solution(N):
    # 한자리수 (1~9) : 9개
    # 두자리수 (10~99) : 90개
    if len(str(N)) <= 2:
        print(N)
        return

    hansu = 9 + 90
    # 세자리수부터 계산
    if 100 <= N and N <= 1000 :
        for i in range(100, N+1):
            if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
                hansu += 1
    print(hansu)


if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
