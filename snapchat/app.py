from geofence import Edge, Vertex, GeoFence
import datetime

nw_corner_manhattan = Edge(40.815, -73.959)
ne_corner_manhattan = Edge(40.801, -73.933)
sw_corner_manhattan = Edge(40.714, -73.015)
se_corner_manhattan = Edge(40.708, -73.011)

manhattan_vertex_north = Vertex(ne_corner_manhattan, nw_corner_manhattan)
manhattan_vertex_west = Vertex(nw_corner_manhattan, sw_corner_manhattan)
manhattan_vertex_south = Vertex(sw_corner_manhattan, se_corner_manhattan)
manhattan_vertex_east = Vertex(se_corner_manhattan, ne_corner_manhattan)

manhattan_geofence_nye_promotion = GeoFence(
    vertices=[
        manhattan_vertex_north,
        manhattan_vertex_west,
        manhattan_vertex_south,
        manhattan_vertex_east,
    ],
    lifetime=datetime.timedelta(hours=24),
)

print(
    [
        (e.latitude, e.longitude)
        for v in manhattan_geofence_nye_promotion.vertices
        for e in [v.edge1, v.edge2]
    ]
)
print(manhattan_vertex_north.length())

# Another way to code the list comprehension above
# lat_longs = []
# for v in manhattan_geofence_nye_promotion.vertices:
#     for e in [v.edge1, v.edge2]:
#         lat_longs.append((e.latitude, e.longitude))
# print(lat_longs)

manhattan_vertex_north.edge1.latitude = 40.847
manhattan_vertex_north.edge1.longitude = -73.886

print(
    [
        (e.latitude, e.longitude)
        for v in manhattan_geofence_nye_promotion.vertices
        for e in [v.edge1, v.edge2]
    ]
)
print(manhattan_vertex_north.length())
