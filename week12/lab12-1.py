import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)
df = pd.DataFrame(X_scaled, columns=iris.feature_names)
df['cluster'] = clusters
df['true_label'] = y
for c in sorted(df['cluster'].unique()):
    most_common_label = (
        df[df['cluster'] == c]['true_label']
        .value_counts()
        .idxmax()
    )
    print(f"Cluster {c}: {target_names[most_common_label]}")