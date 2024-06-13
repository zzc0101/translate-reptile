from utils.load_data import load_pickle_data
from utils.log_config import get_logger
from selenium_task.bing_selenium import translate_text
import pandas as pd
import time, random

# 函数启动
if __name__ == '__main__':
    logging = get_logger()
    
    data_dp = data_list = pd.read_excel('./translate_sample.xlsx', index_col=None)

    data_list = data_dp.iloc[:, 0].tolist()

    # data_list = load_pickle_data()

    start = 0
    end = 200

    logging.info(f"bing翻译开始启动 - 开始索引:{start} - 结束索引：{end}")
    # print(f"bing翻译开始启动 - 开始索引:{start} - 结束索引：{end}")
    list = []

    index = 0
    while True:
        index += 1
        if (start+1) < end:
            if index != 1:
                time.sleep(random.randint(20, 31))
            current_list, start = translate_text(data_list, start, end)
            logging.info(f"bing翻译结束翻译 - 当前索引：{start}")
            # print(f"bing翻译结束翻译 - 当前索引：{start}")
            list.extend(current_list)
        else:
            break

        if index % 100 == 0:
            logging.error('翻译次数超过100次，停止翻译')
            # print('翻译次数超过10次，停止翻译')
            break


    # # 将列表转换为DataFrame
    df = pd.DataFrame(list, columns=["索引", "原文", "翻译"])
    
    # # 保存到Excel文件
    output_file = "./source_data/bing_translate_simple.xlsx"
    df.to_excel(output_file, index=False)
    logging.info("bing翻译结束翻译，并保存文件")
    # print("bing翻译结束翻译，并保存文件")