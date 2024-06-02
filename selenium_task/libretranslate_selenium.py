from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 翻译文本
def translate_text(text_list, start, end):
    # 初始化Chrome浏览器
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 如果不需要可视化，可以使用无头模式
    options.add_argument('--incognito')
    # options.add_argument('--start-maximized')  # 以最大化模式启动
    options.add_argument('--disable-gpu')  # 避免某些系统问题
    # options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"' )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=options)

    # 访问Google翻译页面
    driver.get("https://libretranslate.com/?source=en&target=zh&q=")

    # 刷新一下浏览器
    driver.refresh()

    data_list = []

    try:
        for i in range(start, end):
            result_data = ''
            text_to_translate = text_list[i]
            data = [i+1, text_to_translate]
            # 增加超时时间
            timeout = 10
            # 定位到输入框
            input = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.ID, 'textarea1'))  # 修改为更具体的翻译结果元素定位
            )
            input.clear()
            print(f"原文：{text_to_translate}")
            # 输入文本
            input.send_keys(text_to_translate)
            while True:
                # 获取翻译结果
                content = driver.execute_script("return document.getElementById('%s').value;" % 'textarea2')
                if content != '' and result_data != content:
                    result_data = content
                    data.append(content)
                    break
                time.sleep(1)
            # 打印翻译结果
            # print(f"Translation: {content}")
            data_list.append(data)
            data = []
            for i in range(3):
                time.sleep(i)
    except Exception as e:
        print(f'翻译失败，错误信息：{e}')
    finally:
        # 关闭浏览器
        driver.quit()
        # 返回列表
        return data_list