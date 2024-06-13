import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
df = pd.read_excel("pix2pix(WGAN-GP).xlsx", sheet_name='Sheet2')

# Extract data for plotting
epochs = df["epoch"]
d_loss = df["D loss"]
g_loss = df["G loss"]
pixel_loss = df["pixel"]
adv_loss = df["adv"]
d_loss_sa = df["D loss（自注意力机制）"]
g_loss_sa = df["G loss（自注意力机制）"]
pixel_loss_sa = df["pixel（自注意力机制）"]
adv_loss_sa = df["adv（自注意力机制）"]
d_loss_ca = df["D loss（通道注意力机制）"]
g_loss_ca = df["G loss（通道注意力机制）"]
pixel_loss_ca = df["pixel（通道注意力机制）"]
adv_loss_ca = df["adv（通道注意力机制）"]
d_loss_wgan_gp = df["D loss(WGAN-GP)"]
g_loss_wgan_gp = df["G loss(WGAN-GP)"]
pixel_loss_wgan_gp = df["pixel(WGAN-GP)"]
adv_loss_wgan_gp = df["adv(WGAN-GP)"]


# Plotting
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Plot D loss
axs[0, 0].plot(epochs, d_loss, label='D loss', color='blue', linestyle='-')
axs[0, 0].plot(epochs, d_loss_sa, label='D loss (Self Attention)', color='red', linestyle='--')
axs[0, 0].plot(epochs, d_loss_ca, label='D loss (Channel Attention)', color='green', linestyle='-.')
axs[0, 0].plot(epochs, d_loss_wgan_gp, label='D loss (WGAN-GP)', color='orange', linestyle=':')
axs[0, 0].set_title('D loss')
axs[0, 0].legend()

# Plot G loss
axs[0, 1].plot(epochs, g_loss, label='G loss', color='blue', linestyle='-')
axs[0, 1].plot(epochs, g_loss_sa, label='G loss (Self Attention)', color='red', linestyle='--')
axs[0, 1].plot(epochs, g_loss_ca, label='G loss (Channel Attention)', color='green', linestyle='-.')
axs[0, 1].plot(epochs, g_loss_wgan_gp, label='G loss (WGAN-GP)', color='orange', linestyle=':')
axs[0, 1].set_title('G loss')
axs[0, 1].legend()

# Plot adv loss
axs[1, 0].plot(epochs, adv_loss, label='adv loss', color='blue', linestyle='-')
axs[1, 0].plot(epochs, adv_loss_sa, label='adv loss (Self Attention)', color='red', linestyle='--')
axs[1, 0].plot(epochs, adv_loss_ca, label='adv loss (Channel Attention)', color='green', linestyle='-.')
axs[1, 0].plot(epochs, adv_loss_wgan_gp, label='adv loss (WGAN-GP)', color='orange', linestyle=':')
axs[1, 0].set_title('Adv loss')
axs[1, 0].legend()

# Plot pixel loss
axs[1, 1].plot(epochs, pixel_loss, label='pixel loss', color='blue', linestyle='-')
axs[1, 1].plot(epochs, pixel_loss_sa, label='pixel loss (Self Attention)', color='red', linestyle='--')
axs[1, 1].plot(epochs, pixel_loss_ca, label='pixel loss (Channel Attention)', color='green', linestyle='-.')
axs[1, 1].plot(epochs, pixel_loss_wgan_gp, label='pixel loss (WGAN-GP)', color='orange', linestyle=':')
axs[1, 1].set_title('Pixel loss')
axs[1, 1].legend()

# Adjust layout
plt.tight_layout()
plt.show()

