from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browers_options import get_chrome_driver
from utils.log_config import get_logger
import time, random
import pyperclip

# 翻译文本
def translate_text(text_list, start, end):
    logging = get_logger()
    # 获取浏览器连接驱动配置
    driver =  get_chrome_driver()

    # 访问Google翻译页面
    driver.get("https://www.bing.com/translator?mkt=zh-CN")

    data_list = []

    current_index = 0

    count = 0

    try:
        for i in range(start, end):
            count += 1
            current_index = i
            result_data = ''
            text_to_translate = text_list[i]
            data = [i+1, text_to_translate]
            # 增加超时时间
            timeout = 10
            # 定位到输入框
            input = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.ID, 'tta_input_ta'))
            )
            input.clear()
            logging.info(f"原文：{text_to_translate}")
            pyperclip.copy(text_to_translate)
            # print(f"原文：{text_to_translate}")
            # 输入文本
            input.send_keys(Keys.CONTROL, 'v')
            sleep_index = 0
            while True:
                # 获取翻译结果
                sleep_index += 1
                if sleep_index > 60:
                    raise Exception('翻译超时！！')
                content = driver.execute_script("return document.getElementById('%s').value;" % 'tta_output_ta')
                # 内容不能为空、不能以 ' ...' 结尾同时当前翻译结果不能和上一条结果一致
                if content != '' and result_data != content and not content.endswith(' ...'):
                    result_data = content
                    data.append(content)
                    break
                time.sleep(1)
                print(f'当前超时时长：{sleep_index}')
            # 打印翻译结果
            # print(f"Translation: {content}")
            data_list.append(data)
            data = []
            # 随机休眠，用于模拟人在操作
            time.sleep(random.randint(2, 5))

            # 执行100条数据刷新一次界面
            if count % 100 == 0:
                count = 0
                driver.refresh()
            
    except Exception as e:
        # print(f'翻译失败，错误信息：{e}')
        logging.error(f'翻译失败，错误信息：{e}')
    finally:
        # 关闭浏览器
        driver.quit()
        # 返回列表
        return data_list, current_index

