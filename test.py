import datetime
from calendar import monthrange

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

current_time = datetime.datetime.now()
print(current_time.day)

print(monthrange(current_time.year, 1))

for r in range(1, 6):
    print(r)

print('S{0}-{1}-{0}'.format('me', 'I'))