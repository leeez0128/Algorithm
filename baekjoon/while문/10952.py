import sys
input = sys.stdin.readline

if __name__ == '__main__':
    while(True):
        A, B = map(int, input().strip().split())
        if(A!=0 and B!=0):
            print(A+B)
        else:
            sys.exit(0)       