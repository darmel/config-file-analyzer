from xml.dom import minidom
import sys


file=sys.argv[1]
print("archivo:")
print(file)

# parse an xml file by name
mydoc = minidom.parse(file)

region = mydoc.getElementsByTagName('region')
region=(region[0].attributes['name'].value)

grade= mydoc.getElementsByTagName('grade')
grade=grade[0].attributes['value'].value

print(f"region: {region}")
print(f"grade: {grade}")

""" print(items)
# one specific item attribute
print('Item #2 attribute:')
print(items[1].attributes['name'].value)

# all item attributes
print('nAll attributes:')
for elem in items:
    print(elem.attributes['name'].value)

# one specific item's data
print('\nItem #2 data:')
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

# all items data
print('nAll item data:')
for elem in items:
    print(elem.firstChild.data)  """