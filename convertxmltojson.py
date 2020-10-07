from json import dumps
from xmltodict import parse
from time import strftime

# convert xml to json and save the xml and json in one file.

with open(r'C:\folder-path\inputfile.xml', 'r') as fd:
    contents = fd.read()
    first = parse(contents)

output_file = r'C:\folder-path\output' + strftime("%Y%m%d-%H%M%S") + '.txt'
with open(output_file, 'w') as fw:
    fw.write(dumps(first, indent=4, sort_keys=True))
    fw.write("\n")
    fw.write(contents)
