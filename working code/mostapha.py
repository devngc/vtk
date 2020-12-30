import vtk

Points = vtk.vtkPoints()
Triangles = vtk.vtkCellArray()
Triangle = vtk.vtkTriangle()

Points.InsertNextPoint(1.0, 0.0, 0.0)
Points.InsertNextPoint(0.0, 0.0, 0.0)
Points.InsertNextPoint(0.0, 1.0, 0.0)

Triangle.GetPointIds().SetId(0, 0)
Triangle.GetPointIds().SetId(1, 1)
Triangle.GetPointIds().SetId(2, 2)
Triangles.InsertNextCell(Triangle)

polydata = vtk.vtkPolyData()
polydata.SetPoints(Points)
polydata.SetPolys(Triangles)
polydata.Modified()

## ------------------- ##
# create a data field
df = vtk.vtkFieldData()
temperature = vtk.vtkIntArray()
temperature.SetName("Temperature")
temperature.InsertNextValue(10)
temperature.InsertNextValue(20)
temperature.InsertNextValue(30)
temperature.InsertNextValue(40)

df.AddArray(temperature)

# add data field to polydata
polydata.SetFieldData(df)
## ------------------- ##

writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName('c:/ladybug/test.vpt')
writer.SetInputData(polydata)
writer.Write()