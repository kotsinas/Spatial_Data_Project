import pymorton as pm

class Polygon:
    
    def __init__(self, id):
        self.id = id
        self.coords = []
        self.mbr = []
        self.zcode = 'empty'
    
    def add_coord(self, coord):
        self.coords += [coord]
    
    def set_MBR(self):
        x_min = self.coords[0][0]
        x_max = self.coords[0][0]
        y_min = self.coords[0][1]
        y_max = self.coords[0][1]
        # find the min and max coordinates of the polygon
        for point in self.coords:
            x_min = min(x_min,point[0])
            x_max = max(x_max,point[0])
            y_min = min(y_min,point[1])
            y_max = max(y_max,point[1])
        # calculate the coordinates of the minimum bounding rectangle
        
        #mbr =[float(x_min), float(x_max), float(y_min), float(y_max)]
        mbr = [x_min, x_max, y_min, y_max]
        self.mbr = mbr
    
    def set_zcode(self):
        center_x = (self.mbr[0] + self.mbr[1])/2
        center_y = (self.mbr[2] + self.mbr[3])/2
        self.zcode = pm.interleave_latlng(center_y, center_x)

    def __str__(self):
        return f'id: {self.id}, total coords: {len(self.coords)}'