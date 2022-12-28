import sys
from Range_queries import get_Rtree, get_queries
from kNN_queries import kNN

if len(sys.argv) != 4:
    raise Exception("Invalid arguments.")  

args = sys.argv[1:]
rtree_filename, nn_queries_filename, k = args 
k = int(k)

## Load Rtree and NNqueries from the given filenames
rtree = get_Rtree(rtree_filename)
nn_queries = get_queries(nn_queries_filename)

## Access the root node
root_id = rtree[-1][1]

## Apply NN queries.
count = 0
for i_q, q in enumerate(nn_queries):
    k_nearest_neighbors = kNN(root_id, q, k)
    print(f"{i_q}: {k_nearest_neighbors}")