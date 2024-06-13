import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
# 设置全局字体
matplotlib.rcParams['font.family'] = 'SimSun'  # 使用宋体字体

import warnings
warnings.filterwarnings('ignore', category=UserWarning)

# 读取Excel数据
data = pd.read_excel('随机种子、建筑面积、占地面积、UTCI.xlsx')

# 提取数据
utci_min = data['UTCI']
area_inverse = data['建筑面积倒数']
area = data['占地面积']

# 创建绘图对象
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 绘制3D散点图
scatter = ax.scatter(area_inverse, area, utci_min, c=utci_min, cmap='coolwarm', alpha=0.8)

# 添加颜色标注
cbar = plt.colorbar(scatter)
cbar.set_label('UTCI', fontsize=12)

# 设置坐标轴标签
ax.set_xlabel('建筑面积倒数', fontsize=12)
ax.set_ylabel('占地面积', fontsize=12)
ax.set_zlabel('UTCI', fontsize=12)

# 设置图标题
plt.title('UTCI与建筑面积倒数、占地面积相互关系', fontsize=14)

# 显示图形
plt.show()