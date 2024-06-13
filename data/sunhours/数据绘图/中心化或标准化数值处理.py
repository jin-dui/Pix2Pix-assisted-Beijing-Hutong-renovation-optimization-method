import pandas as pd

# 读取Excel文件
df = pd.read_excel('替换0.01.xlsx')

# 标准化处理
df_normalized = (df - df.mean()) / df.std()

# 构建新的文件名
new_filename = '替换0.01——标准化后的值.xlsx'

# 保存标准化后的数据到新的Excel文件
df_normalized.to_excel(new_filename, index=False)