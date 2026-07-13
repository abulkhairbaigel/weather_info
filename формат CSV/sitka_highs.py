# Теперь можно добавить в график низкую температуру.
# Чтобы ее добавить нам нужно извлечь информацию о ней из файла.  

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение дат, минимальных и максимальных температур из файла.
dates, highs, lows = [], [], []    # создается список lows для хранения мин. температур.
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])   # программа извлекает и сохраняет минимум t для каждой даты из 6-ой позиции каждой строки данных
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Создание диаграммы высоких и низких температур.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')   # вызов plot() окрашивают мин. t в синий цвет

# Форматирование диаграммы.
ax.set_title("Ежедневная максимальная и минимальные температуры, 2021", fontsize=24)   # обновляем заголовок диаграммы.
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Температура (Фаренгейт)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()