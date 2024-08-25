import numpy as np
class Cluster:
     def __init__(self, centroid):
          self.centroid=centroid
          self.points=[]
     def add_points(self,point):
          self.points.append(point)
     def update_centroid(self):
          if len(self.points)>0:
               self.centroid=np.mean(self.points,axis=0)
               self.points=[]
     def get_centroid(self):
          return self.centroid
     def clear_points(self):
          self.points=[]