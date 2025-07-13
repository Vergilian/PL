n, m = map(int, input().split())
circle = list(range(1, n + 1))

path = []
start_index = 0
start_value = circle[start_index]
print(start_value)

path.append(start_value)

while True:
    end_index = (start_index + m - 1) % n
    next_start = circle[end_index]


    if next_start == start_value:
        break

    path.append(next_start)
    start_index = end_index

print(' '.join(map(str, path)))