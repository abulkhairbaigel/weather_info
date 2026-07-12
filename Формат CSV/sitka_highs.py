# Мы можем улучшить диаграмму темп. данных, извлекая даты ежедневных показаний 
# максимальных температур и накладывая их на ось x.

from pathlib import Path
import csv
from datetime import datetime   # импортируем модуль datetime, он нужен для представления строкового формата даты в числовой.

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение максимальных температур.
dates, highs = [], []      # мы создаем 2 пустых списка для хранения дат и температур из файла.
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')   # программа преобразует данные, содержащие информацию даты(row[2]), в объект datetime.
    high = int(row[4])
    dates.append(current_date)      # присоединяем переменную к списку.
    highs.append(high)

# Нанесение данных на диаграмму.
plt.style.use('seaborn-v0_8-paper')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')    # значение дат и температур передаются plot().

# Форматирование диаграммы.
ax.set_title("Ежедневная максимальная температура, Июль 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()      # вызов этой функции выводит метки дат по диагонали, чтобы они не перекрывались.
ax.set_ylabel("Температура (Фаренгейт)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()