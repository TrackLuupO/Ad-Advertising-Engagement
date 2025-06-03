# scatterplot_generator.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
# Replace this with actual data in practice
data = pd.DataFrame({
    'Ad Relevance': [2, 4, 3, 5, 1, 4, 5, 3, 4, 2],
    'Weekly Usage (min)': [120, 240, 180, 300, 90, 260, 320, 150, 270, 110]
})

plt.figure(figsize=(6, 4))
sns.regplot(x='Ad Relevance', y='Weekly Usage (min)', data=data, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.title("Ad Relevance vs Weekly App Usage")
plt.xlabel("Ad Relevance Rating")
plt.ylabel("Weekly App Usage (Minutes)")
plt.tight_layout()
plt.savefig("charts/scatterplot_ad_relevance_vs_usage.png")
plt.show()
