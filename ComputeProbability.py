import csv

first_ball_numbers = {}
second_ball_numbres = {}
first_number_range = 38
second_number_range = 8  
first_total = 0
second_total = 0
scale = 1000000

#初始化資料
def initialBallNumbers():
	for index in range(first_number_range):
		first_ball_numbers[str(index+1)] = 0
	for index in range(second_number_range):
		second_ball_numbres[str(index+1)] = 0

#載入資料
def inputData():
	global first_total, second_total
	with open("data2.csv", newline='') as csvfile:
		#讀取csv
		data = csv.reader(csvfile, delimiter=',')
		x = 0
		for row in data:
			for index in range(len(row)):
				#第一區
				if(x == 1):
					first_total += int(row[index])
				#第二區
				if(x == 2):
					if(index == 8): break
					second_total += int(row[index])
			computeProbability(row, x)
			x += 1

#輸出資料
def outputData():
	global first_ball_numbers, second_ball_numbres
	with open('data3.csv', 'w', newline='') as csvfile:
		# 將 dictionary 寫入 CSV 檔
  		writer = csv.DictWriter(csvfile, fieldnames=first_ball_numbers.keys())
  		# 寫入第一列的欄位名稱
		writer.writeheader()
  		# 寫入資料
  		writer.writerow(first_ball_numbers)
  		writer.writerow(second_ball_numbres)

#計算機率
def computeProbability(row_data, x):
	global first_total, second_total
	for index in range(len(row_data)):
		#第一區
		if(x == 1):
			temp = (int(row_data[index])/first_total)*scale
			first_ball_numbers[str(index+1)] = int(round(temp, 0))
		#第二區
		if(x == 2):
			if(index == 8): return
			temp = (int(row_data[index])/second_total)*scale
			second_ball_numbres[str(index+1)] = int(round(temp, 0))


if __name__ == '__main__':
	initialBallNumbers()
	inputData()
	outputData()
	print(first_total)
	print(second_total)
	print(first_ball_numbers)
	print(second_ball_numbres)
