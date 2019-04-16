import DBSCAN

db = DBSCAN.dbscan(False)
db.feed('./data/network_mix1_point.csv')
#db.cluster(0.001, 10)
#db.cluster(0.0007, 5)
db.cluster(0.0008, 6)
#db.cluster(0.001, 8)