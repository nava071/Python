import shutil
from time import strftime

# Another way to draft related things in a single file and save
# them in another file with a timestamp and reuse the same input file to draft other things.

original = r'C:\folder-path\testdata.txt'
destiny = r'C:\folder-path\testdata' + strftime("%Y%m%d-%H%M%S") + '.txt'
shutil.copy(original, destiny)
