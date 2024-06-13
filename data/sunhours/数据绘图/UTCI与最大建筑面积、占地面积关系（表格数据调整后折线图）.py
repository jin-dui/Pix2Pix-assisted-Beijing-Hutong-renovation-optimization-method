import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 读取Excel文件，指定sheet名称为"Sheet2"
data = pd.read_excel('随机种子、建筑面积、占地面积、UTCI——280条数据.xlsx', sheet_name='Sheet2')

# 提取建筑密度、容积率和UTCI最小列数据
building_density = data['建筑密度']
plot_ratio = data['容积率']
utci_min = data['UTCI']

# 创建子图，共享横轴
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

# 绘制建筑密度变化
ax1.plot(building_density, color='red', marker='o', markersize=5)
ax1.set_ylabel('建筑密度')
ax1.set_title('建筑密度、容积率和UTCI的变化')

# 绘制容积率变化
ax2.plot(plot_ratio, color='green', marker='o', markersize=5)
ax2.set_ylabel('容积率')

# 绘制UTCI变化
ax3.plot(utci_min, color='blue', marker='o', markersize=5)
ax3.set_xlabel('行')
ax3.set_ylabel('UTCI')
# 每隔5个点绘制一个黑色小圆圈
#for i, val in enumerate(utci_min):
#    if i % 5 == 0:
#        ax3.plot(i, val, color='black', marker='o', markersize=3)

# 设置横坐标刻度
xticks = range(0, len(data), 5)
ax3.set_xticks(xticks)

# 在每个刻度处绘制垂直虚线并相连
for x in xticks:
    ax1.axvline(x=x, color='gray', linestyle='--', alpha=0.5)
    ax2.axvline(x=x, color='gray', linestyle='--', alpha=0.5)
    ax3.axvline(x=x, color='gray', linestyle='--', alpha=0.5)

# 调整子图之间的间距
plt.tight_layout()

# 显示图像
plt.show()