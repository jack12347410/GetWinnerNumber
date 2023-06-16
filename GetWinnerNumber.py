import csv
import random
import ComputeProbability as cp

first_ball_numbers = {}
second_ball_numbres = {}
first_ball_range = []
second_ball_range = []

#初始化選區
def initialBallRange():
	global first_ball_range, second_ball_range
	first_ball_range = [i+1 for i in range(cp.first_number_range)]
	second_ball_range = [i+1 for i in range(cp.second_number_range)]

#初始化各號碼的機率
def initialBallNumbers(x, row_data):
	if(x == 1):
		for index in range(len(row_data)):
			first_ball_numbers[str(index+1)] = int(row_data[index])
	if(x == 2):
		for index in range(len(row_data)):
			if(index == 8): return
			second_ball_numbres[str(index+1)] = int(row_data[index])

#set第一區機率陣列
def setFirstRandomList():
	global first_ball_numbers
	temp = []
	count = 0
	while count < cp.scale:
		data = random.choice(first_ball_range)
		if(first_ball_numbers[str(data)] != 0):
			temp.append(data)
			first_ball_numbers[str(data)] -= 1
			count+=1
		elif(first_ball_numbers[str(data)] == 0):
			first_ball_range.remove(data)
	random.shuffle(temp)
	return temp

#set第二區機率陣列
def setSecondRandomList():
	global second_ball_numbres
	temp = []
	count = 0
	while count < cp.scale:
		data = random.choice(second_ball_range)
		if(second_ball_numbres[str(data)] != 0):
			temp.append(data)
			second_ball_numbres[str(data)] -= 1
			count+=1
		elif(second_ball_numbres[str(data)] == 0):
			second_ball_range.remove(data)
	random.shuffle(temp)
	return temp

#選出中獎號碼
def getWinnerNumber(li1, li2, groups):
	for index in range(groups):
		temp = []
		count = 0
		while(count < 6):
			number = random.choice(li1)
			if not(number in temp):
				temp.append(number)
			#li = removeAll(li, number)
				count +=1
		temp.append(random.choice(li2))
		print(temp)

#載入資料
def inputData():
	global first_total, second_total
	with open("data3.csv", newline='') as csvfile:
		#讀取csv
		data = csv.reader(csvfile, delimiter=',')
		x = 0
		for row in data:
			initialBallNumbers(x, row)
			x += 1

#移除list中所有相同的元素
def removeAll(li, el):
	count = 0
	while (el in li):
		print(count)
		li.remove(el)
		count+= 1
	return li

#擴大機率總數後選取中獎號碼
if __name__ == '__main__':
	initialBallRange()
	inputData()
	first_random_list = setFirstRandomList()
	second_random_list = setSecondRandomList()
	getWinnerNumber(first_random_list, second_random_list,6)
