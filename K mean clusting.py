import matplotlib.pyplot as plt
import numpy as np

# Step 1: Set up initial parameters
k = int(input("Enter the number of clusters (K): "))
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'cyan', 'magenta']
tolerance = 1e-4

# Randomly initialize centroids
xc = np.random.rand(k) * 10
yc = np.random.rand(k) * 10

# Sample data points
x = [7.140484932845048, 0.7621359749281376, 0.01964966931324419, 3.283625760370027, 9.883486603985657, 9.80455308506285, 5.157681228979467, 2.2021100868452015, 6.128964446656654, 1.6152275206280153]
y = [9.9771326116337846, 5.866867440927098, 2.216373083540699, 5.282882945169403, 0.3989111558089853, 7.962315116320976, 6.019854320309622, 1.2225895206942494, 0.700240649037791, 4.13513252653905]

# Step 2: Start iterative K-means clustering
plt.figure(figsize=(10, 10))
while True:
    clusters = [[] for _ in range(k)]  # Holds points assigned to each cluster
    
    # Step 3: Assign each point to the nearest centroid
    for i in range(len(x)):
        distances = [np.sqrt((xc[c] - x[i])**2 + (yc[c] - y[i])**2) for c in range(k)]
        min_index = distances.index(min(distances))
        clusters[min_index].append((x[i], y[i]))
    
    # Step 4: Update centroids based on assigned points
    new_xc = []
    new_yc = []
    for c in range(k):
        if clusters[c]:  # Avoid division by zero if a cluster has no points
            new_xc.append(np.mean([point[0] for point in clusters[c]]))
            new_yc.append(np.mean([point[1] for point in clusters[c]]))
        else:  # If no points are assigned, retain the previous centroid
            new_xc.append(xc[c])
            new_yc.append(yc[c])

    # Plot the points and centroids
    plt.clf()  # Clear the previous plot
    for i, cluster in enumerate(clusters):
        cluster_x = [point[0] for point in cluster]
        cluster_y = [point[1] for point in cluster]
        plt.scatter(cluster_x, cluster_y, color=colors[i])

    # Plot centroids
    plt.scatter(new_xc, new_yc, s=100, color='black', marker='x', label="Centroids")

    # Step 5: Check for convergence
    if np.allclose(xc, new_xc, atol=tolerance) and np.allclose(yc, new_yc, atol=tolerance):
        break
    else:
        xc, yc = new_xc, new_yc  # Update centroids for next iteration

plt.grid(True)
plt.legend()
plt.show()
