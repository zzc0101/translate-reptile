from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle, time
import pyperclip

# 加载 pickle 数据
def load_pickle_data():
    with open('contents.pkl', 'rb') as f:
        load_data = pickle.load(f)
    return load_data

def translate_text(text_list, start, end):
    # 初始化Chrome浏览器
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 如果不需要可视化，可以使用无头模式
    options.add_argument('--incognito')
    options.add_argument('--disable-gpu')  # 避免某些系统问题
    options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"' )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
  
    driver = webdriver.Chrome(options=options)

    # 访问Google翻译页面
    driver.get("https://www.bing.com/translator?mkt=zh-CN")

    for i in range(start, end):
        text_to_translate = text_list[i]
        # 增加超时时间
        timeout = 10
        # 定位到输入框
        input = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, 'tta_input_ta'))
        )
        input.clear()
        print(f"原文：{text_to_translate}")
        # 输入文本
        input.send_keys(text_to_translate)
        # 等待翻译结果显示
        # 定位到要复制的元素
        output = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, 'tta_copyIcon'))
        )
        time.sleep(10)
        element = driver.find_element(By.ID, 'tta_copyIcon')
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        # 模拟选中元素内容
        # element_to_copy.click()
        # 等待一小段时间，确保复制操作完成
        time.sleep(1)
        copied_content = pyperclip.paste()
        # 打印翻译结果
        print(f"Translation: {copied_content}")
        for i in range(3):
            time.sleep(i)

    # 关闭浏览器
    driver.quit()

# 调用函数
translate_text(load_pickle_data(), 100000, 200000)
# print(load_pickle_data()[0])
