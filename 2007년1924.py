x, y = map(int, input().split())

week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 0

for i in range(x - 1):
    day += month[i]

day = (day + y) % 7

print(week[day])