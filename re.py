import os

#=========================================================
# Clean up - Remove all files with misc extensions
#=========================================================
filelist = [ f for f in os.listdir(".") if f.endswith(".xls") ]
for f in filelist:
    os.remove(f)
filelist = [ f for f in os.listdir(".") if f.endswith(".txt") ]
for f in filelist:
    os.remove(f)
filelist = [ f for f in os.listdir(".") if f.endswith(".html") ]
for f in filelist:
    os.remove(f)
