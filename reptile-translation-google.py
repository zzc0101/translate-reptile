from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

# 加载 pickle 数据
def load_pickle_data():
    with open('contents.pkl', 'rb') as f:
        load_data = pickle.load(f)
    return load_data

# def load_urls():
#     # 这里加载你的URL列表
#     urls = ['https://www.mi.com', 'https://www.apple.com', 'https://www.tesla.com']
#     return urls

def open_and_interact_with_pages(driver, urls):
    # 打开第一个页面
    driver.get(urls[0])

    # 遍历剩余的URL，打开新标签页并进行操作
    for url in urls[1:]:
        # 使用JavaScript在新标签页中打开URL
        driver.execute_script("window.open('" + url + "','_blank');")

        # 等待新窗口出现并切换到它
        new_window = WebDriverWait(driver, 5).until(
            EC.number_of_windows_to_be(2)
        )
        driver.switch_to.window(driver.window_handles[-1])

        # 在新打开的页面上执行操作
        # 假设我们想要等待页面加载完成后再继续
        page_load_wait = WebDriverWait(driver, 10)
        page_load_wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # 例如，我们可以模拟用户点击某个按钮
        button = driver.find_element(By.XPATH, '//button[text()="Click me"]')
        button.click()

        # 等待一段时间，让操作生效
        time.sleep(2)

    # 返回到初始页面
    driver.switch_to.window(driver.window_handles[0])


def open_multiple_browsers():
    # 创建指定数量的浏览器实例
    screen_width = 1920  # 请替换为你的屏幕宽度
    screen_height = 1080  # 请替换为你的屏幕高度
    # 初始化Chrome浏览器
    options = webdriver.ChromeOptions()
    # options.add_argument('--incognito')
    quarter_width = int(screen_width / 2)
    quarter_height = int(screen_height / 2)
    # 设置窗口大小
    options.add_argument(f"--window-size={quarter_width},{quarter_height}")
    options.add_argument('--start-maximized')  # 以最大化模式启动
    driver = webdriver.Chrome(options=options)
    # 每次迭代创建一个新的浏览器实例
    driver = webdriver.Chrome(options=options)

    # 在每个浏览器中打开一个网页
    # url = num_browsers[i]  # 假设你有多个不同的URL
    driver.get('https://translate.google.com/?hl=zh-CN&sl=en&tl=zh-CN&text=hey&op=translate')

    # 在这里执行浏览器实例上的操作，如点击、输入等
    

    # 在完成操作后，关闭该浏览器实例
    driver.quit()


if __name__ == "__main__":
    open_multiple_browsers()
    time.sleep(100)