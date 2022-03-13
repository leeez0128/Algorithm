import sys
input = sys.stdin.readline


def hanoi(N, src, dest, via):
	if N == 1:
		print(src, dest)
	else:
		hanoi(N-1, src, via, dest)
		print(src, dest)
		hanoi(N-1, via, dest, src)


if __name__ == '__main__':
    N = int(input().strip())
    print(2**N-1)
    hanoi(N, 1, 3, 2)