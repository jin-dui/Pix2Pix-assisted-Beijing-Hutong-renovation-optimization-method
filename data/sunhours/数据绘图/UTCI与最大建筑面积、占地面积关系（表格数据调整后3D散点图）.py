import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Arial Unicode MS'
from mpl_toolkits.mplot3d import Axes3D

# 读取Excel文件，指定sheet名称为"Sheet2"
data = pd.read_excel('随机种子、建筑面积、占地面积、UTCI.xlsx', sheet_name='Sheet2')

# 提取建筑密度、容积率和UTCI最小列数据
building_density = data['建筑密度']
plot_ratio = data['容积率']
utci_min = data['UTCI']

# 设置3D散点图的图形和坐标轴
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 创建3D散点图
ax.scatter(building_density, plot_ratio, utci_min, c=utci_min, cmap='coolwarm', s=80)

# 设置坐标轴标签
ax.set_xlabel('建筑密度')
ax.set_ylabel('容积率')
ax.set_zlabel('UTCI')

# 设置标题
ax.set_title('建筑密度、容积率和UTCI之间的关系')

# 显示图像
plt.show()