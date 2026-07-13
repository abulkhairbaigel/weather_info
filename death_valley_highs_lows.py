# Иногда данных в некоторых числах могут отсутствовать, надо преждевременно с этим бороться.
# Для этого и существуют исключения.

# TOBS - данные за конкретное время наблюдений, которые регистрирует станция.
# Внесите изменения в sitka_highs_lows.py. чтобы создать график температур для Долины смерти.

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[3])
    low = int(row[4])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Ежедневная максимальная и минимальные температуры, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Температура (Фаренгейт)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

# Код был изменен, но у нас вылезает ошибка.
# В трассировке указано, что Python не сможет обработать tmax для одной из дат, 
# поскольку не сумеет преобразовать пустую строку ('') в целое число.