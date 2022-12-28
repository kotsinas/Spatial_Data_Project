from Polygon import Polygon

def get_polygon_list(offsets_filename, coords_filename):

    offsets = open(offsets_filename, 'r')
    fcoords = open(coords_filename, 'r')

    coords = [line.split(',') for line in fcoords.readlines()]

    polygons_to_return = []
    for line in offsets.readlines():
        id, startOffset, endOffset = line.split(',')

        polyon_to_create = Polygon(id)
        polygons_to_return += [polyon_to_create]

        for i_coord in range(int(startOffset), int(endOffset) + 1):
            x = float(coords[i_coord][0].replace('\n', '')); 
            y = float(coords[i_coord][1].replace('\n', ''))
            polyon_to_create.add_coord( (x, y) )

    offsets.close()
    fcoords.close()

    return polygons_to_return


def calculate_MBRs(polygons):
    for p in polygons:
        p.set_MBR()
    return polygons 

def calculate_zcodes(polygons):
    for p in polygons:
        p.set_zcode()
    return polygons 

