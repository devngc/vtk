import vtk

# Adding points
points = vtk.vtkPoints()
points.InsertNextPoint(0.0, 0.0, 0.0)
points.InsertNextPoint(5.0, 0.0, 0.0)
points.InsertNextPoint(5.0, 0.0, 5.0)
points.InsertNextPoint(0.0, 0.0, 5.0)

# Creating a Polygon out of points
polygon = vtk.vtkPolygon()
polygon.GetPointIds().SetNumberOfIds(4)  # make a quad
polygon.GetPointIds().SetId(0, 0)
polygon.GetPointIds().SetId(1, 1)
polygon.GetPointIds().SetId(2, 2)
polygon.GetPointIds().SetId(3, 3)

# Adding polygons
polygons = vtk.vtkCellArray()
polygons.InsertNextCell(polygon)

# colors = vtk.vtkNamedColors()
# Colors = vtk.vtkUnsignedCharArray()
# Colors.SetNumberOfComponents(3)
# Colors.SetName("Colors")
# Colors.InsertNextTuple3(*colors.GetColor3ub('Red'))

numbers = vtk.vtkFloatArray()
numbers.SetName('Numbers')
numbers.InsertNextValue(0.1)

polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetPolys(polygons)


polydata.GetCellData().SetScalars(numbers)


# write an XML file
# writer = vtk.vtkXMLPolyDataWriter()
# writer.SetFileName('sample.vtp')
# writer.SetInputData(polydata)
# writer.Write()


## ------------------- ##
# create a data field
df = vtk.vtkFieldData()
temperature = vtk.vtkStringArray()
temperature.SetName("Colors")
temperature.InsertNextValue("Red")

df.AddArray(temperature)

# add data field to polydata
polydata.SetFieldData(df)
## ------------------- ##

polydata.Modified()


# Write a vtk file
writer = vtk.vtkPolyDataWriter()
writer.SetFileName('sample.vtk')
writer.SetInputData(polydata)
writer.Write()