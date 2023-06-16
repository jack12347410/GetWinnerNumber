# coding: utf-8
import random

def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))
    print(randnum)

    for index, scope in enumerate(rate):
        start += scope
        print(start)
        if randnum <= start:
            break
    print(index)
    return index

def main():
    arr = ['red', 'green', 'blue']
    rate = [45, 30, 25]

    red_times = 0
    green_times = 0
    blue_times = 0
    for i in range(10000):
        if arr[random_index(rate)] == 'red':
            red_times += 1
        if arr[random_index(rate)] == 'green':
            green_times += 1
        if arr[random_index(rate)] == 'blue':
            blue_times += 1

    print(red_times, green_times, blue_times)

if __name__ == '__main__':
    #main()
    random_index([45, 30, 25])
