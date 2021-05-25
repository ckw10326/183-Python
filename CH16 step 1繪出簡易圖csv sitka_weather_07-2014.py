# =============================================================================
# import csv
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)
#     
# #打印文件头及其位置
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)
#         
# # 从文件中获取最高气温
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     
#     highs = []
#     for row in reader:
#         high = int(row[1])
#         highs.append(high)
#     print(highs)
# =============================================================================

'''P532 绘制气温图表
import csv
from matplotlib import pyplot as plt

# 从文件中获取最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    print(enumerate(header_row))
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)

# =============嘗試讀取row[2]失敗===============================================
#     lows = []
#     for row in reader:
#         low = int(row[10])
#         lows.append(low)
#     print(lows)
# =============================================================================
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
'''
import csv
from matplotlib import pyplot as plt
from datetime import datetime
# 从文件中获取日期和最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
#繪製成斜線
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()