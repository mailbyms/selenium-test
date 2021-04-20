from selenium import webdriver
import time
import threading

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

capabilities = options.to_capabilities()

class myThread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        print ("开始线程：", self.threadID)
        work(self.threadID)
        print ("退出线程：", self.threadID)

def work(threadID):
    driver = webdriver.Remote( \
          command_executor='http://192.168.1.70:4444/wd/hub', \
            desired_capabilities=capabilities)
    # 启动浏览器，获取网页源代码
    url = "https://www.baidu.com/"
    driver.get(url)
    print(driver.title)
    time.sleep(3)
    driver.quit()

# 创建新线程
thread1 = myThread(1)
thread2 = myThread(2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")



