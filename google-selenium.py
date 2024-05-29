from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle, time, pyperclip

# 加载 pickle 数据
def load_pickle_data():
    with open('contents.pkl', 'rb') as f:
        load_data = pickle.load(f)
    return load_data

def translate_text(text_list):
    # 初始化Chrome浏览器
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 如果不需要可视化，可以使用无头模式
    # options.add_argument('--incognito')
    options.add_argument('--start-maximized')  # 以最大化模式启动
    options.add_argument('--disable-gpu')  # 避免某些系统问题
    options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"' )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=options)

    # 访问Google翻译页面
    driver.get("https://translate.google.com")

    for i in text_list:
        text_to_translate = i
        # 增加超时时间
        timeout = 10
        # 定位到输入框
        input = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, '//*[@aria-label="原文"]'))  # 修改为更具体的翻译结果元素定位
            # EC.presence_of_element_located((By.CLASS_NAME, 'er8xn'))
        )
        # 将数据写入剪贴板
        pyperclip.copy(i)

        input.clear()
        print(f"原文：{text_to_translate}")
        # 输入文本

        driver.execute_script("arguments[0].value = arguments[1];", input, pyperclip.paste())
        input.send_keys(Keys.RETURN)

        # input.send_keys(text_to_translate)
        # 等待翻译结果显示
        translation_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@jsname="jqKxS"]'))
            # EC.presence_of_element_located((By.CLASS_NAME, 'lRu31'))  # 修改为更具体的翻译结果元素定位
        )
        # 获取翻译结果
        translated_text = translation_result.text
        # 打印翻译结果
        print(f"Translation: {translated_text}")
        time.sleep(10000)

    # 关闭浏览器
    driver.quit()

# 调用函数
translate_text(load_pickle_data())
# print(load_pickle_data()[0])