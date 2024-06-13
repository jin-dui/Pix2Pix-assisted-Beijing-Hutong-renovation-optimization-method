import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 读取Excel文件，指定sheet名称为"Sheet2"
data = pd.read_excel('随机种子、建筑面积、占地面积、UTCI.xlsx', sheet_name='Sheet2')

# 提取建筑密度、容积率和UTCI最小列数据
building_density = data['建筑密度']
plot_ratio = data['容积率']
utci_min = data['UTCI']

# 创建2D散点图
plt.scatter(building_density, plot_ratio, c=utci_min, cmap='coolwarm', s=80)

# 设置坐标轴标签
plt.xlabel('建筑密度')
plt.ylabel('容积率')

# 添加颜色图例和标签
cbar = plt.colorbar()
cbar.set_label('UTCI')

# 设置标题
plt.title('建筑密度、容积率和UTCI之间的关系')

# 显示图像
plt.show()