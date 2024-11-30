import sys

array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
n = 5

min_v = sys.maxsize * 2 + 1
min_i = 0
min_j = 0
count_iterations = 0

for i in range(n):
    for j in range(n):
        if array[i][j] <= min_v:
            min_v = array[i][j]
            min_i = i
            min_j = j
        count_iterations += 1
        print(array[i][j], end=' ')

print(count_iterations)

n = 7

array_sim = [[1, 2, 3, 4, 5, 6, 7], [2, 6, 7, 8, 9, 6, 7], [3, 7, 10, 11, 12, 6, 7], [4, 8, 11, 13, 14, 6, 7], [5, 9, 12, 14, 15, 6, 7], [1, 2, 3, 4, 5, 6, 7], [2, 6, 7, 8, 9, 6, 7]]

min_v = sys.maxsize * 2 + 1
min_i = 0
min_j = 0
count_iterations = 0

for i in range(n):
    for j in range(i, n):
        if array_sim[i][j] <= min_v:
            min_v = array[i][j]
            min_i = i
            min_j = j
        count_iterations += 1
        print(array_sim[i][j], end=' ')

print(count_iterations)

n = 7

array_roads = [[1, 2, 3, 4, 5, 6, 7], [2, 6, 7, 8, 9, 6, 7], [3, 7, 10, 11, 12, 6, 7], [4, 8, 11, 13, 14, 6, 7], [5, 9, 12, 14, 15, 6, 7], [1, 2, 3, 4, 5, 6, 7], [2, 6, 7, 8, 9, 6, 7]]

min_v = sys.maxsize * 2 + 1
min_i = 0
min_j = 0
count_iterations = 0

for i in range(n-1):
    for j in range(i+1, n):
        if array_roads[i][j] <= min_v:
            min_v = array[i][j]
            min_i = i
            min_j = j
        count_iterations += 1
        print(array_roads[i][j], end=' ')

print(count_iterations)
