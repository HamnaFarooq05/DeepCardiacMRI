import matplotlib.pyplot as plt

# Values confirmed from earlier classification analysis
features = ["EF %", "ESV mL", "Myo Mass g", "EDV mL"]
importance = [0.314706, 0.295590, 0.249347, 0.140357]

colors = ["#4C72B0", "#55A868", "#DD8452", "#C44E52"]

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.barh(features, importance, color=colors, edgecolor="black", linewidth=0.8)

for bar, val in zip(bars, importance):
    ax.text(bar.get_width() + 0.005, bar.get_y() + bar.get_height()/2,
            f"{val*100:.1f}%", va="center", fontsize=10)

ax.set_xlabel("Feature Importance")
ax.set_title("Random Forest Feature Importance for Pathology Classification")
ax.set_xlim(0, 0.38)
ax.invert_yaxis()  # highest importance at top

plt.tight_layout()
plt.savefig("feature_importance.png", dpi=150, bbox_inches="tight")
print("Saved!")