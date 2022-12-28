from Range_queries import *
import math
import heapq 

def get_distance(q,mbr):
    point_x = q[0]
    point_y = q[1]

    #define the coordinates of the MBR
    mbr_x1 = mbr[0]
    mbr_x2 = mbr[1]
    mbr_y1 = mbr[2]
    mbr_y2 = mbr[3]

    #calculate the distance between the point and the MBR
    #first, calculate the distance between the point and the closest corner
    dist1 = math.sqrt((point_x - mbr_x2)**2 + (point_y - mbr_y2)**2)

    #second, calculate the distance between the point and the farthest corner
    dist2 = math.sqrt((point_x - mbr_x1)**2 + (point_y - mbr_y1)**2)

    distance = max(dist1, dist2)
    return distance
   
def get_MBRcenter(mbr):
    center_x = (mbr[0] + mbr[1])/2
    center_y = (mbr[2] + mbr[3])/2
    return [center_x, center_y]


def kNN(rootID, q_point, k):

    nearest_neighbors = []
    pr_queue = []
    
    rootnode = get_node(rootID)
    rootMBR = get_MBR(rootnode[2])
    heapq.heappush(pr_queue, (get_distance(q_point, rootMBR), rootID))

    isnoleaf = True
    while isnoleaf:

        dist, nodeID = heapq.heappop(pr_queue)
        node = get_node(nodeID)
        
        for child in node[2]:
            heapq.heappush(pr_queue, (get_distance(q_point, child[1]), child[0]))

        if node[0] == 0:
            isnoleaf = False
            print()
        
            for i in range(k):
                dist, nodeID = heapq.heappop(pr_queue)
                nearest_neighbors.append(nodeID)
 

    return nearest_neighbors

def get_MBR(children):
    x_array=[]
    y_array=[]

    for child in children:
        
        x_array.append(float(child[1][0]))
        x_array.append(float(child[1][1]))
        y_array.append(float(child[1][2]))
        y_array.append(float(child[1][3]))

    x_low=min(x_array)
    x_high=max(x_array)
    y_low=min(y_array)
    y_high=max(y_array)

    return [float(x_low), float(x_high), float(y_low), float(y_high)]
    
kNNqueries = get_queries('NNqueries.txt')
rootID = rtree[-1][1]
# print(get_node(rootID))




