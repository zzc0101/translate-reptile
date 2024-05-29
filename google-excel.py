import pickle
import pandas as pd

# 加载 pickle 数据
def load_pickle_data():
    with open('contents.pkl', 'rb') as f:
        load_data = pickle.load(f)
    return load_data

data = load_pickle_data()

list = []

index = 0

for i in data:
    print(i)
    index += 1
    list.append(i)
    if index == 100000:
        break    

df = pd.DataFrame(list, columns=['原文'])

# 将DataFrame写入Excel文件
df.to_excel('output.xlsx', index=False)
