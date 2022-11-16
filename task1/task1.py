from collections import deque
from itertools import cycle
n = int(input())
m = int(input())

path = []

cycle = cycle([i + 1 for i in range(n)])
selection = deque([next(cycle) for i in range(m)], maxlen=m)
path.append(selection[0])

while selection[-1] != 1:
        # итерация с конца предыдущего массива
        for i in range(m - 1):
            selection.append(next(cycle))
            # записываем путь
        path.append(selection[0])
print (''.join(map(str, path)))