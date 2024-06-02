from utils.load_data import load_pickle_data, get_data_len
from selenium_task.libretranslate_selenium import translate_text
import pandas as pd

# 函数启动
if __name__ == '__main__':
    data_list = load_pickle_data()

    list = translate_text(data_list, 1999999, get_data_len())

    # 将列表转换为DataFrame
    df = pd.DataFrame(list, columns=["索引", "原文", "翻译"])
    
    # 保存到Excel文件
    output_file = "libretranslate_one.xlsx"
    df.to_excel(output_file, index=False)