import chroma
from chroma.demo.optics import glass, water, vacuum

g = chroma.geometry.Geometry(water)
length = 50
width = 0.5
boxX = chroma.make.box(length, width, width, center=(length/2, width/2, width/2))
boxY = chroma.make.box(width, length, width, center=(width/2, length/2, width/2))
boxZ = chroma.make.box(width, width, length, center=(width/2, width/2, length/2))
X = chroma.geometry.Solid(boxX, glass, water, surface=None, color=0xFF9900) #orange
Y = chroma.geometry.Solid(boxY, glass, water, surface=None, color=0xff0000) #red
Z = chroma.geometry.Solid(boxZ, glass, water, surface=None, color=0x33FF00) #green
g.add_solid(X, rotation=None, displacement=None)
g.add_solid(Y, rotation=None, displacement=None)
g.add_solid(Z, rotation=None, displacement=None)
chroma.view(g)
