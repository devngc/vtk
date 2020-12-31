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


polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetPolys(polygons)
polydata.Modified()

# Write a vtk file
# writer = vtk.vtkPolyDataWriter()
# writer.SetFileName('sample.vtk')
# writer.SetInputData(polydata)
# writer.Write()

# writer = vtk.vtkXMLPolyDataWriter()
# writer.SetFileName('sample.vtp')
# writer.SetInputData(polydata)
# writer.Write()


writer = vtk.vtkJSONDataSetWriter()
writer.SetFileName('sample')
writer.SetInputData(polydata)
writer.Write()
