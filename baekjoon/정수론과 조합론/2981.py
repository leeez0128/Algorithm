import sys, math
input = sys.stdin.readline

def solution(numbers):
    difference = []
    for i in range(1, len(numbers)):
        difference.append(abs(numbers[i]-numbers[i-1]))

    gcd_ = math.gcd(*difference)
    result = [gcd_]
        
    for i in range(2, int(gcd_**(1/2))+1):
        if gcd_ % i == 0:
            result.append(i)
            if i != (gcd_//i):
                result.append(gcd_//i)

    print(" ".join(map(str, sorted(result))))


if __name__ == '__main__':
    N = int(input().strip())
    numbers = []
    for _ in range(N):
        numbers.append(int(input().strip()))

    solution(numbers)
