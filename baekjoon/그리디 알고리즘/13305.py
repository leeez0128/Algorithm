import sys
input = sys.stdin.readline


def solution(cities, city_km, liter_price):
    small_price = liter_price[0]
    total_price = 0

    for i in range(cities-1):
        if liter_price[i] < small_price:
            small_price = liter_price[i]
        total_price += small_price * city_km[i]

    print(total_price)


if __name__ == '__main__':
    cities = int(input().strip())
    city_km = list(map(int, input().strip().split()))
    liter_price = list(map(int, input().strip().split()))
    solution(cities, city_km, liter_price)
