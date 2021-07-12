from math import sin, cos, sqrt, atan2
import datetime

# approximate radius of Earth in km
R = 6373.0


class Edge:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.coords = (latitude, longitude)


class Vertex:
    def __init__(self, edge1, edge2):
        self.edge1 = edge1
        self.edge2 = edge2

    def length_longitude(self):
        return self.edge1.longitude - self.edge2.longitude

    def length_latitude(self):
        return self.edge1.latitude - self.edge2.latitude

    def length(self):
        return (
            R
            * 2
            * atan2(
                sqrt(
                    sin(self.length_latitude() / 2) ** 2
                    + cos(self.edge1.latitude)
                    * cos(self.edge2.latitude)
                    * sin(self.length_longitude() / 2) ** 2
                ),
                sqrt(
                    1
                    - sin(self.length_latitude() / 2) ** 2
                    + cos(self.edge1.latitude)
                    * cos(self.edge2.latitude)
                    * sin(self.length_longitude() / 2) ** 2
                ),
            )
        )

    # def update(self, edge1=None, edge2=None):
    #     if all(not x for x in [edge1, edge2]):
    #         raise Exception('Must provide at least one edge to update')
    #     if edge1 and not edge2:
    #         return Vertex(edge1, self.edge2)
    #     elif edge2 and not edge1:
    #         return Vertex(self.edge1, edge2)
    #     else:
    #         return Vertex(edge1, edge2)


class GeoFence:
    def __init__(self, vertices, lifetime):
        self.vertices = vertices
        self.lifetime = lifetime
        self.created_time = datetime.datetime.now()

    def is_expired(self):
        return datetime.datetime.now() - self.lifetime > self.created_time
