import matplotlib.pyplot as plt
import numpy as np

models = ["U-Net", "Attention U-Net", "TransUNet"]
params = [7.7, 31.4, 21.7]       # millions
inference = [15.81, 22.31, 13.64]  # ms
memory = [137, 284, 330]          # MB

colors = ["#4C72B0", "#DD8452", "#55A868"]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, data, title, ylabel in zip(
    axes,
    [params, inference, memory],
    ["Parameters (Millions)", "Inference Time (ms)", "Memory Usage (MB)"],
    ["Parameters (M)", "Time (ms)", "Memory (MB)"]
):
    bars = ax.bar(models, data, color=colors, edgecolor="black", linewidth=0.8)
    ax.set_title(title, fontsize=12)
    ax.set_ylabel(ylabel)
    for bar, val in zip(bars, data):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(data)*0.02,
                f"{val}", ha="center", fontsize=10)
    ax.set_ylim(0, max(data)*1.2)

plt.suptitle("Computational Efficiency Comparison Across Models", fontsize=14)
plt.tight_layout()
plt.savefig("efficiency_comparison.png", dpi=150, bbox_inches="tight")
print("Saved!")