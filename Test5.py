from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv

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
    #SuperLottoValue.append(submitKey)
    #print(submitKey)
    # 提交表單
    driver.find_element_by_xpath("//*[@id='SuperLotto638Control_history1_btnSubmit']").click()
    searchData(driver)
    #print(SuperLottoValue)

# 取得資料
def searchData(driver):
	if is_element_exist(driver, super_lotto_ids[0]):
		print("exist")
	else:
		print("null")
	#for super_lotto_id in super_lotto_ids:
		#data = driver.find_element_by_id(super_lotto_id).text
		#if not data: 
		#	print("null")
		#else:
		#	print(data)
		#SuperLottoValue.append(data)

#此元素是否存在
def is_element_exist(driver, css):
    s = driver.find_elements_by_id(css)
    if len(s) == 0:
        return False
    else:
        return True

# 方法主入口
if __name__ == '__main__':
	driver = openChrome()
	try:
		for y in range(110):
			nextKey = 108000110 - y
			print(nextKey)
			operationAuth(driver, nextKey)
	finally:
	 	closeChrome(driver)