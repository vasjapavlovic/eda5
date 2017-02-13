import sys
sys.path.append('/usr/lib/freecad/lib')
import FreeCAD
import Part
import Drawing
from FreeCAD import Base



Part.show(Part.makeBox(100,100,100).cut(Part.makeCylinder(80,100)).cut(Part.makeBox(90,40,100)).cut(Part.makeBox(20,85,100)))

Shape = App.ActiveDocument.Shape.Shape # this is where it breaks
[visibleG0,visibleG1,hiddenG0,hiddenG1] = Drawing.project(Shape)
print "visible edges:", len(visibleG0.Edges)
print "hidden edges:", len(hiddenG0.Edges)

[visibleG0,visibleG1,hiddenG0,hiddenG1] = Drawing.project(Shape,Base.Vector(1,1,1))

resultSVG = Drawing.projectToSVG(Shape,App.Vector(1,1,1))
print resultSVG
