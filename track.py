# model of the track
import random
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

#@param length/radius in meters
class Segment:
    length = 0
    radius = 0
    x = 0
    y = 0
    next = 0
    
    def __init__(self, name, x, y, length, radius):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.length = length
        
    def __str__(self):
        return f"<Name: {self.name}, x: {self.x}, y: {self.y}, Length: {self.length}, Radius: {self.radius}>"
    

class Track:
    start = 0
    curr = 0
    numSeg = 0
    d = {}        
    
    def __init__(self, *args):
        if isinstance(args[0], int):
            c = 'A'
            oldX = 10
            oldY = 10
            self.d[c] = Segment(c, oldX, oldY, 0, 0)
            self.start = self.d[c]
            self.curr = self.start
            self.numSeg = args[0]
            
            for i in range(args[0]-1):
                c = chr(ord(c)+1)
                if oldX <= 50 and oldY <= 50:
                    self.d[c] = Segment(c, random.randint(oldX,100), random.randint(oldY,50), 0, 0)
                elif oldX <= 50 and oldY >= 50:
                    self.d[c] = Segment(c, random.randint(oldX,50), random.randint(0,oldY), 0, 0)
                elif oldX >= 50 and oldY <= 50:
                    self.d[c] = Segment(c, random.randint(50,oldX), random.randint(oldY,100), 0, 0)
                elif oldX >= 50 and oldY >= 50:
                    self.d[c] = Segment(c, random.randint(0,oldX), random.randint(50,oldY), 0, 0)
                oldX = self.d[c].x 
                oldY = self.d[c].y
                self.curr.next = self.d[c]
                self.curr = self.curr.next
                
            self.curr.next = self.start
            self.curr = self.start 
        elif isinstance(args[0], str):
            self.d["S0"] = Segment("S0", 10, 10, 1, 0)
            self.d["S1"] = Segment("S1", 30, 10, 1, 0)
            self.d["S2"] = Segment("S2", 80, 20, 1, 0)
            self.d["S3"] = Segment("S3", 90, 70, 1, 0)
            self.d["S4"] = Segment("S4", 50, 80, 1, 0)
            self.d["S5"] = Segment("S5", 30, 70, 1, 0)
            self.d["S6"] = Segment("S6", 20, 40, 1, 0)
            self.d["S7"] = Segment("S7", 10, 20, 1, 0)
            self.d["S0"].next = self.d["S1"]
            self.d["S1"].next = self.d["S2"]
            self.d["S2"].next = self.d["S3"]
            self.d["S3"].next = self.d["S4"]
            self.d["S4"].next = self.d["S5"]
            self.d["S5"].next = self.d["S6"]
            self.d["S6"].next = self.d["S7"]
            self.d["S7"].next = self.d["S0"]
            self.start = self.d["S0"]
            self.curr = self.start
            self.numSeg = 8
        for i in range(self.numSeg):
            self.curr.length = round(math.sqrt(self.curr.x*self.curr.x + self.curr.next.y*self.curr.next.y), 3)
            self.curr = self.curr.next
            
    
    def __str__(self):
        out = ""
        for i in range(self.numSeg):
            out += str(self.curr) + "\n"
            self.curr = self.curr.next
        return out      
    
    def getSeg(self) -> Segment:
        seg = self.curr
        self.curr = self.curr.next
        return seg
    
    def getLength(self, a , b) -> int:
        segA = self.d[a]
        segB = self.d[b]
        length = segA.length
        segA = segA.next
        while segA != segB:
            length += segA.length
            segA = segA.next
        return round(length,3)
    
# testing    
t = Track("manual")

print(t)
print("S0 -> S0: " + str(t.getLength("S0", "S0")))
print("S0 -> S2: " + str(t.getLength("S0", "S2")))
print("S6 -> S7: " + str(t.getLength("S6", "S7")))
# print("A -> A: " + str(t.getLength("A", "A")))
# print("A -> C: " + str(t.getLength("A", "C")))
# print("C -> D: " + str(t.getLength("C", "D")))

verts = []
for i in range(t.numSeg):
    seg = t.getSeg()
    verts.append((seg.x,seg.y))
verts.append((0,0))

codes = []
codes.append(Path.MOVETO)
for i in range(t.numSeg-1):    
    codes.append(Path.LINETO)
codes.append(Path.CLOSEPOLY)

path = Path(verts, codes)

fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
plt.show()