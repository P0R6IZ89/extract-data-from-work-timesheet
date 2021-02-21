import datetime
from calendar import monthrange

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

current_time = datetime.datetime.now()
print(current_time.day)

print(monthrange(current_time.year, 1))
for n in range(10, 12):
    for r in range(1, 6):
        if r == 4:
            # r += 1
            break
        print(n)
        print(r)
        
