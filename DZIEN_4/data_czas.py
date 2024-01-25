import datetime
from datetime import date
import time

print(f'minimalny rok daty: {datetime.MINYEAR}')
print(f'maksymalny rok daty: {datetime.MAXYEAR}')

print(f'zadana data to: {datetime.date(1994,11,23)}')
print(f'dzisiejsza data: {date.today()}')

print(f'minimalna data: {date.min}')
print(f'maksymalna data: {date.max}')

print(f"Czas liczony sekundach (TS) od epoki: {date.fromtimestamp(1_690_854_335)}")

obj = time.gmtime(0)
epoka = time.asctime(obj)
print(f'epoka: {epoka}')
time_sec = time.time()

print(f"czas [s] od epoki to aktualnego momentu czasowego: {time_sec} s")
