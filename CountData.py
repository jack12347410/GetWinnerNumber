import csv
first_ball_numbers = {}
second_ball_numbres = {}
first_number_range = 38
second_number_range = 8  

def inputData():
	with open("data1.csv", newline='') as csvfile:
		#讀取csv
		data = csv.reader(csvfile, delimiter=',')
		x = 0
		for row in data:
			if(x != 0):
				computeNumbers(row)
			x += 1

def initialBallNumbers():
	for index in range(first_number_range):
		first_ball_numbers[str(index+1)] = 0
	for index in range(second_number_range):
		second_ball_numbres[str(index+1)] = 0

def computeNumbers(row_data):
	for index in range(len(row_data)):
		if(index != 0):
			if(index == 7): 
				second_ball_numbres[str(row_data[index])] += 1
				return	
			first_ball_numbers[str(row_data[index])] += 1

def outputData():
	with open('data2.csv', 'w', newline='') as csvfile:
		# 將 dictionary 寫入 CSV 檔
		writer = csv.DictWriter(csvfile, fieldnames=first_ball_numbers.keys())
		# 寫入第一列的欄位名稱
		writer.writeheader()
  		# 寫入資料
		writer.writerow(first_ball_numbers)
		writer.writerow(second_ball_numbres)
		print(first_ball_numbers)
		print(second_ball_numbres)

def convertData():
	for index in range(first_number_range):
		first_ball_numbers[str(index+1)] = str(first_ball_numbers[str(index+1)])
	for index in range(second_number_range):
		second_ball_numbres[str(index+1)] = str(second_ball_numbres[str(index+1)])

if __name__ == '__main__':
	initialBallNumbers()
	inputData()
	outputData()
