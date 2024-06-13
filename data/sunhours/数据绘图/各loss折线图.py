import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel数据
data = pd.read_excel('pix2pix日志数据整理（200epoch）.xlsx')

# 提取各列数据
epochs = data['epoch']
d_loss = data['D loss:']
g_loss = data['G loss:']
pixel_loss = data['pixel:']
adv_loss = data['adv:']

# 创建绘图对象
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制 D loss 折线和散点
ax1.plot(epochs, d_loss, label='D loss', color='r')
ax1.scatter(epochs, d_loss, color='r')

# 绘制 Pixel loss 折线和散点
ax1.plot(epochs, pixel_loss, label='Pixel loss', color='b')
ax1.scatter(epochs, pixel_loss, color='b')

# 绘制 Adv loss 折线和散点
ax1.plot(epochs, adv_loss, label='Adv loss', color='c')
ax1.scatter(epochs, adv_loss, color='c')

# 设置坐标轴标签
ax1.set_xlabel('Epoch', fontsize=14)
ax1.set_ylabel('D loss / Pixel loss / Adv loss', fontsize=14)

# 创建第二个坐标轴（右侧）
ax2 = ax1.twinx()

# 绘制 G loss 折线和散点
ax2.plot(epochs, g_loss, label='G loss', color='g')
ax2.scatter(epochs, g_loss, color='g')

# 设置坐标轴标签
ax2.set_ylabel('G loss', fontsize=14)

# 设置图例
ax1.legend(fontsize=12, loc='upper left')
ax2.legend(fontsize=12, loc='upper right')

# 调整坐标轴范围
ax1.set_xlim(left=0, right=200)

# 调整坐标轴刻度位置
ax2.yaxis.tick_right()

# 显示图形
plt.show()