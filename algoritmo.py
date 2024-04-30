import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.cluster import DBSCAN
from sklearn_extra.cluster import KMedoids
from sklearn.preprocessing import StandardScaler

# Cargar los datos
data = {
    'Id': [1, 2, 3, 4, 5],
    'VALOR_ESTIMADO': [100, 200, 300, 400, 500],
    'VALOR_ESTIMADO_ADQUISICIONES': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Preprocesamiento de datos
df_clean = df.fillna(df.mean())
X = df_clean[['VALOR_ESTIMADO', 'VALOR_ESTIMADO_ADQUISICIONES']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar K-Means
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans_labels = kmeans.fit_predict(X_scaled)

# Aplicar Gaussian Mixture Models (GMM)
gmm = GaussianMixture(n_components=2, random_state=0)
gmm_labels = gmm.fit_predict(X_scaled)

# Aplicar DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=2)
dbscan_labels = dbscan.fit_predict(X_scaled)

# Aplicar K-Medoids
kmedoids = KMedoids(n_clusters=2, random_state=0)
kmedoids_labels = kmedoids.fit_predict(X_scaled)

# Mostrar resultados
print("K-Means labels:", kmeans_labels)
print("GMM labels:", gmm_labels)
print("DBSCAN labels:", dbscan_labels)
print("K-Medoids labels:", kmedoids_labels)
