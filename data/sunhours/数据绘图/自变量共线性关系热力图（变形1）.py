import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel数据
data = pd.read_excel('基因参数PMV最小AREA最大的400条原始数据（自变量乘以0.03和0.05系数并对应好列名）——标准化后的值.xlsx')

# 提取自变量列
independent_vars = data.iloc[:, 0:14]

# 计算相关性矩阵
correlation_matrix = independent_vars.corr()

# 创建颜色映射
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# 绘制矩形图形式的相关性矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap=cmap, square=True, linewidths=0.5)
plt.title('Correlation Matrix of Independent Variables')

# 添加相关系数数值
for i in range(correlation_matrix.shape[0]):
    for j in range(correlation_matrix.shape[1]):
        if i != j:
            plt.text(j + 0.5, i + 0.5, "{:.2f}".format(correlation_matrix.iloc[i, j]),
                     ha='center', va='center', color='black')

# 调整坐标轴刻度位置
plt.xticks(np.arange(len(correlation_matrix.columns)) + 0.5, correlation_matrix.columns, rotation=90)
plt.yticks(np.arange(len(correlation_matrix.columns)) + 0.5, correlation_matrix.columns, rotation=0)

plt.show()