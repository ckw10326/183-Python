import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取每天的最高温度
filename = 'death_valley_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	# next(reader)函数是返回reader阅读器的下一行，目前只调用了一次，所以是头行
	header_row = next(reader)
	# 打印头行，header_row它是一个列表
	# print(header_row)
	# enumerate() 获取每个元素的索引及其值
	for index, column_header in enumerate(header_row):
		print(index, column_header)

	# 第二列每天的最高温度
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, '错误数据')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

	# 根据数据绘制图形
	fig = plt.figure(dpi=128, figsize=(10, 6))
	plt.plot(dates, highs, c='red')
	plt.plot(dates, lows, c='blue')

	# facecolor指定填充区域的颜色
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
	# 设置图形的格式
	title = "Daily high and low temperatures - 2014\nDeath Valley CA"
	plt.title(title, fontsize=20)
	plt.xlabel("", fontsize=16)
	# 绘制斜的日期标签
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)

	plt.show()


