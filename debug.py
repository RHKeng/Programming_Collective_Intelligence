import clusters
from Manhattan_distance import Manhattan_distance

blognames,words,data=clusters.readfile('blogdata.txt')
clust=clusters.hcluster(data)
clust1=clusters.hcluster(data,distance=Manhattan_distance)

reload(clusters)
clusters.printclust(clust,labels=blognames)
clusters.printclust(clust1,labels=blognames)

print data[0]
print len(data[0])
print data[1]
print len(data[1])
print Manhattan_distance(data[0],data[1])