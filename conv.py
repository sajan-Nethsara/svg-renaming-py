import lxml.etree as ET

# Load the SVG file
tree = ET.parse('output.svg')
root = tree.getroot()

# Define the namespace for SVG elements
namespace = {'svg': 'http://www.w3.org/2000/svg'}
group_id = 'sections'

# Find the specified group
group = root.find(f".//svg:g[@id='{group_id}']", namespace)
# Find and convert polygon elements to path elements
polygons = group.findall('.//svg:polygon', namespace)
for polygon in polygons:
    points = polygon.get('points')
    class_attr = polygon.get('class')
    id_attr = polygon.get('id')
    # Create a new path element
    path_element = ET.Element('path', d=f"M{points} Z" )
    path_element.set('class', class_attr )
    if id_attr is not None:
        path_element.set('id', id_attr)

    # Insert the new path element before the polygon element
    parent = polygon.getparent()
    parent.insert(parent.index(polygon), path_element)

    # Remove the polygon element
    parent.remove(polygon)

# Find and convert rect elements to path elements
rects = root.findall('.//svg:rect', namespace)
for rect in rects:
    x = float(rect.get('x'))
    y = float(rect.get('y'))
    width = float(rect.get('width'))
    height = float(rect.get('height'))
    class_attr = rect.get('class')
    id_attr = rect.get('id')
    # Create a new path element
    path_d = f"M{x} {y} L{x+width} {y} L{x+width} {y+height} L{x} {y+height} Z"
    path_element = ET.Element('path', d=path_d )
    path_element.set('class', class_attr)
    if id_attr is not None:
        path_element.set('id', id_attr)


    # Insert the new path element before the rect element
    parent = rect.getparent()
    parent.insert(parent.index(rect), path_element)

    # Remove the rect element
    parent.remove(rect)

# Save the modified SVG file
tree.write('output14441.svg')