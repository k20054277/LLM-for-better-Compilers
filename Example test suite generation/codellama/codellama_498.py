# Import necessary libraries
from sklearn.cluster import KMeans
import pandas as pd

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('data.csv')

# Use None to indicate that the number of clusters is unknown
kmeans = KMeans(n_clusters=None, random_state=0).fit(df)

# Get the optimal number of clusters from the elbow method
elbow_plot = kmeans.get_elbow()
plt.plot(elbow_plot)
plt.xlabel('Number of Clusters')
plt.ylabel('Sum of Squared Errors')
plt.show()

# Use the optimal number of clusters to perform clustering analysis
kmeans = KMeans(n_clusters=elbow_plot[-1], random_state=0).fit(df)

# Get the cluster labels for each data point
cluster_labels = kmeans.predict(df)

# Print the cluster labels to the console
print(cluster_labels)