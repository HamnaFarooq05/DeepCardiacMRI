import pandas as pd
import matplotlib.pyplot as plt

# Use extended_params.csv if available, else fall back to physiological_params.csv
import os
if os.path.exists("extended_params.csv"):
    df = pd.read_csv("extended_params.csv")
    ef_col = "LV_EF_%" if "LV_EF_%" in df.columns else "EF_%"
else:
    df = pd.read_csv("physiological_params.csv")
    ef_col = "EF_%"

group_order = ["NOR", "DCM", "HCM", "MINF", "RV"]
group_means = df.groupby("Group")[ef_col].mean().reindex(group_order)
group_std = df.groupby("Group")[ef_col].std().reindex(group_order)

colors = {"NOR": "#55A868", "DCM": "#C44E52", "HCM": "#4C72B0", "MINF": "#DD8452", "RV": "#8172B2"}
bar_colors = [colors[g] for g in group_order]

fig, ax = plt.subplots(figsize=(8, 5.5))
bars = ax.bar(group_order, group_means, yerr=group_std, capsize=5,
              color=bar_colors, edgecolor="black", linewidth=0.8)

# Clinical normal range shading
ax.axhspan(55, 70, color="gray", alpha=0.15, label="Normal EF range (55-70%)")

ax.set_ylabel("Ejection Fraction (%)")
ax.set_xlabel("Pathology Group")
ax.set_title("Predicted Ejection Fraction by Pathology Group")
ax.legend(loc="upper right", fontsize=9)
ax.set_ylim(0, 100)

for bar, mean in zip(bars, group_means):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            f"{mean:.1f}%", ha="center", fontsize=10)

plt.tight_layout()
plt.savefig("ef_by_pathology_group.png", dpi=150, bbox_inches="tight")
print("Saved!")