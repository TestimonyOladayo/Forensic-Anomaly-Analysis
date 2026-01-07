import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create a "High-Stakes" Dataset
np.random.seed(42)
n_points = 1000
normal_data = pd.DataFrame({
    'Amount': np.random.normal(500, 100, n_points),
    'Velocity': np.random.normal(10, 2, n_points),
    'Risk_Score': np.random.normal(20, 5, n_points),
    'Type': 'Normal'
})

# 2. Inject "Sophisticated" Anomalies (Clusters)
anomalies = pd.DataFrame({
    'Amount': [2500, 2600, 2450, 100, 150],
    'Velocity': [90, 85, 88, 5, 2],
    'Risk_Score': [95, 98, 92, 80, 85],
    'Type': 'Anomaly'
})

df = pd.concat([normal_data, anomalies])

# 3. Create a Professional Pair Plot
sns.set_theme(style="whitegrid")
g = sns.pairplot(df, hue='Type', palette={'Normal': '#2ecc71', 'Anomaly': '#e74c3c'},
                 diag_kind='kde', plot_kws={'alpha': 0.6})
g.fig.suptitle("Forensic Multi-Dimensional Analysis: Identifying Out-of-Distribution Clusters", y=1.02, fontsize=16)
plt.savefig('forensic_clusters.png')
plt.show()
