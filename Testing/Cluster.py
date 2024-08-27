import numpy as np

class Cluster:
     def __init__(self,centroid):
          self.centroid=centroid
          self.points=[]
          self.diabetes=0
     def assign_point(self,point):
          self.points.append(point)
          if point[-1]==1:
               self.diabetes+=1
     def update_centroid(self):
          if self.points:
               self.centroid=np.mean(self.points,axis=0)
     def get_centroid(self):
          return self.centroid
     def get_diabetes(self):
          return self.diabetes
     def get_length(self):
          return len(self.points)
     def reset_points(self):
          self.points=[]
          self.diabetes=0