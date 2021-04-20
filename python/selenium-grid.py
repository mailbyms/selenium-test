from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

capabilities = options.to_capabilities()

driver = webdriver.Remote( \
          command_executor='http://192.168.1.70:4444/wd/hub', \
            desired_capabilities=capabilities)

# 启动浏览器，获取网页源代码
url = "https://www.baidu.com/"
driver.get(url)

print(driver.title)

time.sleep(3)
driver.quit()


