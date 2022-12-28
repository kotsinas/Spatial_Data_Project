import sys
from init_polygons import get_polygon_list, calculate_zcodes, calculate_MBRs
from tree import construct_tree

if len(sys.argv) != 3:
    raise Exception("Invalid arguments.")  

args = sys.argv[1:]
coords_filename, offsets_filename = args 

polygon_list = get_polygon_list(offsets_filename, coords_filename)
polygon_list = calculate_MBRs(polygon_list)
polygon_list = calculate_zcodes(polygon_list)
sorted_polygon_list = sorted(polygon_list, key=lambda obj:obj.zcode)

tree = construct_tree(sorted_polygon_list, 0, 0, [])

# Storing rtree  in a text file 
with open("Rtree.txt", "w") as file:
    [file.write(str(item) + '\n') for item in tree]
