import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取Excel数据
data = pd.read_excel('基因参数PMV最小AREA最大的400条原始数据（自变量乘以0.03和0.05系数并对应好列名）.xlsx')

# 提取自变量列
independent_vars = data.iloc[:, 0:14]

# 计算相关性矩阵
correlation_matrix = independent_vars.corr()

# 绘制相关性矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Matrix of Independent Variables')
plt.show()