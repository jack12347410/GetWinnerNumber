from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv


SuperLottoKey = ['期別', '第一區_1', '第一區_2', '第一區_3', '第一區_4', '第一區_5', '第一區_6','第二區']
SuperLottoValue = []
SuperLotto = {}
SuperLottoDate = {'108': 62, '107': 105, '106': 104, '105': 104, '104': 103, '103': 104}
NowDate = 108
super_lotto_ids = ['SuperLotto638Control_history1_dlQuery_No1_0','SuperLotto638Control_history1_dlQuery_No2_0',
				'SuperLotto638Control_history1_dlQuery_No3_0','SuperLotto638Control_history1_dlQuery_No4_0',
				'SuperLotto638Control_history1_dlQuery_No5_0','SuperLotto638Control_history1_dlQuery_No6_0',
				'SuperLotto638Control_history1_dlQuery_No7_0']

# 後台開啟瀏覽器模式
def openChrome():
    # 加啟動配置
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    # 開啟chrome瀏覽器
    driver = webdriver.Chrome(options=option)
    return driver

# 關閉瀏覽器
def closeChrome(driver):
	driver.close()
	driver.quit()

# 授權操作
def operationAuth(driver, submitKey):
    url = "https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx"
    driver.get(url)
    # 找到輸入框並輸入查詢內容
    elem = driver.find_element_by_id("SuperLotto638Control_history1_txtNO")
    elem.send_keys(submitKey)
    SuperLottoValue.append(submitKey)
    #print(submitKey)
    # 提交表單
    driver.find_element_by_xpath("//*[@id='SuperLotto638Control_history1_btnSubmit']").click()
    searchData(driver)
    #print(SuperLottoValue)

# 取得資料
def searchData(driver):
	for super_lotto_id in super_lotto_ids:
		data = driver.find_element_by_id(super_lotto_id).text
		SuperLottoValue.append(data)

# 輸出資料成csv
def outputData():
	with open('Test1.csv', 'w', newline='') as csvfile:
		# 將 dictionary 寫入 CSV 檔
  		writer = csv.DictWriter(csvfile, fieldnames=SuperLottoKey)
  		# 寫入第一列的欄位名稱
  		writer.writeheader()
  		# 寫入資料
  		for data in SuperLotto.values():
  			#print(data)
  			writer.writerow(data)

def setData(key):
	print(SuperLottoValue)
	SuperLotto[str(key)] = dict(zip(SuperLottoKey, SuperLottoValue))
	SuperLottoValue.clear()


# 方法主入口
if __name__ == '__main__':
	#print(type(SuperLottoDate['108']))
    # 加啟動配置
    driver = openChrome()

    try:
    	for x in range(len(SuperLottoDate)):
    		nextDate = NowDate - x
    		key = nextDate*1000000 + SuperLottoDate[str(nextDate)]
    		for y in range(SuperLottoDate[str(nextDate)]):
    			nextKey = key - y
    			operationAuth(driver, nextKey)
    			setData(nextKey)
    	outputData()
    finally:
    	closeChrome(driver)
