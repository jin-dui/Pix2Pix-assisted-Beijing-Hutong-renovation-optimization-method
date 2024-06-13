import pandas as pd
import matplotlib.pyplot as plt

# 设置字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 使用支持中文的字体，如Arial Unicode MS
plt.rcParams['axes.unicode_minus'] = False  # 用于正常显示负号

# 读取数据
df = pd.read_excel("pix2pix（自注意力机制）.xlsx")

# 创建画布和子图
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# 颜色和线型设置
line_styles = ['-', '--']
colors = ['blue', 'orange']

# 分别绘制四张图
for i, metric in enumerate(['D loss', 'G loss', 'adv', 'pixel']):
    ax = axs[i // 2, i % 2]  # 选择子图

    # 原始数据
    ax.plot(df['epoch'], df[metric], label=metric, linestyle=line_styles[0], color=colors[0])
    # 自注意力机制数据
    ax.plot(df['epoch'], df[f'{metric}（自注意力机制）'], label=f'{metric}（自注意力机制）', linestyle=line_styles[1],
            color=colors[1])

    # 添加标题和标签
    ax.set_title(metric)
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    ax.legend()

# 调整布局
plt.tight_layout()

# 保存图表
plt.savefig('combined_plot.png')

# 显示图表
plt.show()
