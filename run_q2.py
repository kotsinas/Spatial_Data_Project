import sys
from Range_queries import query, get_Rtree, get_queries

if len(sys.argv) != 3:
    raise Exception("Invalid arguments.")  

args = sys.argv[1:]
rtree_filename, r_queries_filename = args 

## Load Rtree and Rqueries from the given filenames
rtree = get_Rtree(rtree_filename)
rqueries = get_queries(r_queries_filename)

## Access the root node
root_id = rtree[-1][1]

## Apply R queries.
for i_w, w in enumerate(rqueries):
    answer = query(root_id, w, [])
    print(f"{i_w} ({len(answer)}): {answer}")
