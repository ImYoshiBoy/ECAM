import sys

# print the original sys.path
print('Original sys.path:', sys.path)

# append a new directory to sys.path
sys.path.append('/path/to/directory')

# print the updated sys.path
print('Updated sys.path:', sys.path)

# now you can import your module
#import your_module
