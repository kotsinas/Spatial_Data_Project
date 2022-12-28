from Polygon import *

class Rtreenode:

    def __init__(self, id):
        self.id = id
        self.nodeMBR = []
        self.children = []
        self.root = False
        self.leaf = False

    def populate_children(self, node_to_added):
        self.children.append(node_to_added)

    def set_root_node(self):
        self.root = True

    def set_leaf_node(self):
        self.leaf = True

    def set_node_MBR(self):
        x_array=[]
        y_array=[]

        for i in self.children:
            if isinstance(i, Rtreenode):
                x_array.append(float(i.nodeMBR[0]))
                x_array.append(float(i.nodeMBR[1]))
                y_array.append(float(i.nodeMBR[2]))
                y_array.append(float(i.nodeMBR[3]))
            else:
                x_array.append(float(i.mbr[0]))
                x_array.append(float(i.mbr[1]))
                y_array.append(float(i.mbr[2]))
                y_array.append(float(i.mbr[3]))

        x_low=min(x_array)
        x_high=max(x_array)
        y_low=min(y_array)
        y_high=max(y_array)

        self.nodeMBR = [float(x_low), float(x_high), float(y_low), float(y_high)]

    def __str__(self):

        if self.leaf == True:
            leaf = 0
        else:
            leaf = 1

        children_info = []
        for child in self.children:
            if isinstance(child, Rtreenode):
                children_info.append([child.id, child.nodeMBR])
            else:
                children_info.append([child.id, child.mbr])
            
        return (f"{leaf}, {self.id}, {children_info}")

def create_node(id, list_of_20components):

    node = Rtreenode(id)
    id+=1
    for p in list_of_20components:
        node.populate_children(p)

        if isinstance(p, Polygon):
            node.set_leaf_node()
        
        node.set_node_MBR()
        
    return node

def divide__into_chunks(lst):
    n = 20 
    chunked_list = [lst[i * n:(i + 1) * n] for i in range((len(lst) + n - 1) // n )] 

    if len(chunked_list[-1])<8:
        n = 8 - len(chunked_list[-1])
        chunked_list[-1][:0] = chunked_list[-2][-n:]
        del chunked_list[-2][-n:]

    return chunked_list

'''def divide__into_chunks(list):
    if len(list)<=20:
        return list
    
    max_chunk_size = 20
    min_chunk_size = 8
    chunked_list = []
    while len(list) > 0:
        if len(list) > max_chunk_size:
            chunked_list.append(list[:max_chunk_size])
        else:
            remaining = max_chunk_size - len(list)
            if remaining < min_chunk_size:
                chunked_list.append(list[:-remaining])
                chunked_list.append(list[-remaining:])
            else:
                chunked_list.append(list)
        list = list[max_chunk_size:]

    if len(chunked_list[-1])<8:
        n = 8 - len(chunked_list[-1])
        chunked_list[-1][:0] = chunked_list[-2][-n:]
        del chunked_list[-2][-n:]
   
        if len(chunked_list[-2])<8:
            n = 8 - len(chunked_list[-2])
            chunked_list[-2][:0] = chunked_list[-3][-n:]
            del chunked_list[-3][-n:]

    for c in chunked_list:
        if len(c) == 0:
            chunked_list.remove(c)
    
    return chunked_list'''

def construct_tree(sorted_list, lvl, id, tree):
    new_call_list = []

    chunks = divide__into_chunks(sorted_list)

    for chunk in chunks:
        node = create_node(id, chunk)
        tree.append(node)
        new_call_list.append(node)
        id+=1

    print("level =", lvl, 'nodes', len(new_call_list))
    lvl+=1
    
    if len(new_call_list)>20:
        return construct_tree(new_call_list, lvl, id, tree)
    else:
        #root
        root = Rtreenode(id)
        root.set_root_node()

        for root_child in new_call_list:
            root.populate_children(root_child)
        root.set_node_MBR()
        print("level =", lvl, 'nodes', 1)
        tree.append(root)
        return tree



    
    






