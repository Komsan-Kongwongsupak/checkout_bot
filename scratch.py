import datetime

f_time = datetime.datetime(2024, 5, 5, 0, 0)
n_time = datetime.datetime.now()

print(f_time)
print(n_time)
print((f_time - n_time).total_seconds())