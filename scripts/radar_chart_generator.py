# radar_chart_generator.py
import matplotlib.pyplot as plt
import numpy as np

# Labels and data
categories = ['Ad Relevance → Patronage', 'Ad Frequency → Uninstall Risk']
values = [0.81, abs(-0.43)]

# Repeat first value to close chart
values += values[:1]
angles = [n / float(len(categories)) * 2 * np.pi for n in range(len(categories))]
angles += angles[:1]

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], categories, color='black')
plt.yticks([0.2, 0.4, 0.6, 0.8], ["0.2", "0.4", "0.6", "0.8"], color="grey", size=8)
plt.ylim(0, 1)
ax.plot(angles, values, linewidth=2, linestyle='solid')
ax.fill(angles, values, 'skyblue', alpha=0.4)
plt.title("Radar Chart: Institutional Differences", size=12, y=1.1)
plt.tight_layout()
plt.savefig("charts/radar_chart_institutional_differences.png")
plt.show()