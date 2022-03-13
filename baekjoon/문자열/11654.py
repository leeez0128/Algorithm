import sys
input = sys.stdin.readline

# ASCII CODE
# ord(문자) : ordinary를 알아낸다!라고 생각하자
# chr(숫자) : 숫자를 문자로 바꾸는 과정이 아스키!
def solution(v):
    print(ord(v))


if __name__ == '__main__':
    v = input().strip()
    solution(v)
