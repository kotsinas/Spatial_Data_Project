def get_Rtree(Rtree_filename):

    Rtree = open(Rtree_filename, 'r')
    tree = []
    for line in Rtree.readlines():
        tree.append(list(eval(line)))
    Rtree.close()   

    return tree

def get_queries(queries_filename):
    
    range_queries = []
    with open(queries_filename,mode='r') as queries:
        for line in queries.readlines():
            mbr = line.split(' ')
            mbr = line.replace('\n', '')
            mbr = line.replace(' ', ',')
            range_queries.append(list(eval(mbr)))

    if queries_filename == 'Rqueries.txt':
        range_queries = correct_windows_coords(range_queries)

    return range_queries

def get_node(id):
    for node in rtree:
        if id == node[1]:
            return node
        
def query(root_id, window, polygons_to_return):
    node = get_node(root_id)    
    # in node
    if node[0] == 1:
        for child in node[2]:
            if check_intersection(child[1], window) == True:
                query(child[0], window, polygons_to_return)
    # in leave
    else:
        for child in node[2]:
            if check_intersection(child[1], window) == True:
                polygons_to_return.append(child[0])         
    return polygons_to_return

def correct_windows_coords(windows):
    new_coords=[]
    for coord in windows:
        new_coords.append([coord[0], coord[2], coord[1], coord[3]])
    return new_coords

def check_intersection(mbr, window):

    window_x_low, window_x_high, window_y_low, window_y_high = window[0], window[1], window[2], window[3]
    mbr_x_low, mbr_x_high, mbr_y_low, mbr_y_high = mbr[0], mbr[1], mbr[2], mbr[3]

    if ((window_x_high < mbr_x_low) or (window_x_low > mbr_x_high)):
        return False
    elif ((window_y_high < mbr_y_low) or (window_y_low > mbr_y_high)):
        return False
    elif ((window_x_high >= mbr_x_high) and (window_x_low <= mbr_x_low)) and ((window_y_low <= mbr_y_low) and (window_y_high >= mbr_y_high)):
        return True
    elif ((mbr_x_high >= window_x_high) and (mbr_x_low <= window_x_low)) and ((mbr_y_low <= window_y_low) and (mbr_y_high >= window_y_high)):
        return True
    return True


rtree = []
rtree = get_Rtree('Rtree.txt')
Rqueries = get_queries('Rqueries.txt')




