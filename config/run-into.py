import json
import pickle

# 导入pandas模块，用于数据处理和分析
# import pandas as pd

# 打开名为'sites.dat'的文件，以二进制只读模式（'rb'）打开
with open('./sites.dat', 'rb') as f:
    # 使用pickle模块的load函数从文件中加载数据，并将加载的数据存储在变量load中
    load = pickle.load(f)

# 打印输出变量load的内容
# print(load)

# 使用json模块的dumps函数将load变量转换为JSON格式的字符串，然后使用json模块的loads函数将JSON字符串解析为Python对象，并将解析后的对象存储在变量info中
    info = json.dumps(load, indent=2)

# # 输出打印格式化的 JSON 字符串
    print(info)
