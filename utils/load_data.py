import pickle

# 加载 pickle 数据
def load_pickle_data():
    with open('contents.pkl', 'rb') as f:
        load_data = pickle.load(f)
    return load_data


# 统计 pickle 数据长度
def get_data_len():
    load_data = load_pickle_data()
    index = 0
    for i in load_data:
        index += 1
    return index