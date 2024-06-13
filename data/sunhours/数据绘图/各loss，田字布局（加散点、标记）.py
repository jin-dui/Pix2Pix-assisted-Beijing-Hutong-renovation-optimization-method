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
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
fig.subplots_adjust(hspace=0.4)

# 绘制 D loss 图
axes[0, 0].plot(epochs, d_loss, label='D loss', color='r')
axes[0, 0].scatter(epochs, d_loss, marker='o', color='r')
axes[0, 0].set_xlabel('Epoch', fontsize=12)
axes[0, 0].set_ylabel('D loss', fontsize=12)
axes[0, 0].legend(fontsize=10, loc='upper right')
axes[0, 0].spines['right'].set_visible(False)
axes[0, 0].spines['top'].set_visible(False)

# 绘制 G loss 图
axes[0, 1].plot(epochs, g_loss, label='G loss', color='g')
axes[0, 1].scatter(epochs, g_loss, marker='^', color='g')
axes[0, 1].set_xlabel('Epoch', fontsize=12)
axes[0, 1].set_ylabel('G loss', fontsize=12)
axes[0, 1].legend(fontsize=10, loc='upper right')
axes[0, 1].spines['right'].set_visible(False)
axes[0, 1].spines['top'].set_visible(False)

# 绘制 Adv loss 图
axes[1, 0].plot(epochs, adv_loss, label='Adv loss', color='c')
axes[1, 0].scatter(epochs, adv_loss, marker='s', color='c')
axes[1, 0].set_xlabel('Epoch', fontsize=12)
axes[1, 0].set_ylabel('Adv loss', fontsize=12)
axes[1, 0].legend(fontsize=10, loc='upper right')
axes[1, 0].spines['right'].set_visible(False)
axes[1, 0].spines['top'].set_visible(False)

# 绘制 Pixel loss 图
axes[1, 1].plot(epochs, pixel_loss, label='Pixel loss', color='b')
axes[1, 1].scatter(epochs, pixel_loss, marker='*', color='b')
axes[1, 1].set_xlabel('Epoch', fontsize=12)
axes[1, 1].set_ylabel('Pixel loss', fontsize=12)
axes[1, 1].legend(fontsize=10, loc='upper right')
axes[1, 1].spines['right'].set_visible(False)
axes[1, 1].spines['top'].set_visible(False)

# 调整布局
plt.subplots_adjust(wspace=0.3, hspace=0.4)

# 显示图形
plt.show()