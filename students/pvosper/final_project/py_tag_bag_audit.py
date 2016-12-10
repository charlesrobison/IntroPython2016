#!/usr/bin/env python

print('''
\tCreates tag_bag_audit.csv, listing .patterns and .budget_sets from .global_tag_bags
\tAlso creates common_budget_set_audit.csv, listing all .patterns from common budget sets
\t<source file name>, <source file w/relative path>, <referenced tag file name>, <referenced tag file file w/relative path>
''')

import os

import time

start = time.clock()

def extract_tag_name(line_string):
    '''Returns referenced tag name and path given valid string (line from file), otherwise returns None'''
    # Assume any line with quotes is a tag reference
    # 'cd' in 'abcdefg' == True
    if line_string.find('"') >= 0:
        tag_path = line_string[line_string.find('"'):-1]
        s = os.path.basename(tag_path)
        tag_name = s[:s.find(".")]
        entry_list = [tag_name, tag_path.replace('\\\\', '\\').replace('"', '')]
        return(entry_list)
    else:
        return None
        
def source_files():
    '''Returns the source file name given valid path'''
    pass

# This assumes file name == destination name (True in this case)    
# $ToDo: generator expression -> no intermediate array is produced
#   for x in (y for y in items if y > 10):

# Create list of destination tag bags
tag_bag_list = []
# for nt.DirEntry in nt.ScandirIterator
for destination_dir in os.scandir(r'content\world'):
    for file in os.scandir(destination_dir.path):
        if file.name.endswith('.grognok_destination.tft'):
            with open(file.path) as destination:
                lines_list = destination.readlines()
                for i in range(len(lines_list)):
                    if lines_list[i].find('FIELD global_tag_bag') >= 0:
                        # Now read the next 4 lines
                        for j in range(4):
                            if lines_list[i + j].find('FIELD m_referenced_tag_name') >= 0:
                                tag_bag_list.append(extract_tag_name(lines_list[i + j]))
                                # There's only one global_tag_bag entry per destination so we should stop here

print(tag_bag_list)

end = time.clock()
                
if __name__ == "__main__":
    print('\tFinished!\n\tElapsed time: {:.2f} seconds'.format(end - start))