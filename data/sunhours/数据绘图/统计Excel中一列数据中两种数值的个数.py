import pandas as pd

# 读取Excel文件
data = pd.read_excel('基因参数PMV最小AREA最大的400条原始数据（自变量乘以3和5系数并对应好列名）.xlsx')

# 统计0.18和0.21的个数
count_018 = (data['Hor_2 line'] == 0.18).sum()
count_021 = (data['Hor_2 line'] == 0.21).sum()

# 打印结果
print("0.18的个数:", count_018)
print("0.21的个数:", count_021)