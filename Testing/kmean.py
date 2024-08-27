import numpy as np
from Cluster import Cluster
import pandas as pd

def z_scaling(feature):
     return (feature-feature.mean())/feature.std()
def interpolation(feature):
     return (feature-feature.min())/(feature.max()-feature.min())
def assign_point_to(clusters,feature):
     for point in feature:
          distances=[np.linalg.norm(point-cluster.get_centroid()) for cluster in clusters]
          indexx=np.argmin(distances)
          clusters[indexx].assign_point(point)
def update_centroids(clusters):
     for cluster in clusters:
          cluster.update_centroid()
def reset(clusters):
     for cluster in clusters:
          cluster.reset_points()
def k_means(clusters,feature):
     i=0
     while True:
          print("Epoch",i+1)
          prev=[cluster.get_centroid() for cluster in clusters]
          update_centroids(clusters)
          reset(clusters)
          assign_point_to(clusters,feature)
          new=[cluster.get_centroid() for cluster in clusters]
          if np.array_equal(prev,new):
               break
          i+=1
def result(clusters,total_diabetes_patients):
     for i, cluster in enumerate(clusters):
          diabetes_count_in_cluster = cluster.get_diabetes()
          percentage_diabetes_in_cluster = (diabetes_count_in_cluster / total_diabetes_patients) * 100
          print(f"Cluster {i+1} Centroid: {cluster.get_centroid()}")
          print(f"Cluster {i+1} Diabetes Patients: {diabetes_count_in_cluster}")
          print(f"Percentage of Total Diabetes Patients in Cluster {i+1}: {percentage_diabetes_in_cluster:.2f}%")