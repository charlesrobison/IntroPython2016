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

# Create list of destination tag bags
tag_bag_list = []
world_path = r'content\world' # this path is hard-coded into project and cannot change
# Find the name of all directories in \world
for world_dir in os.scandir(world_path):
    # Create path strings for each destination directory
    destination_dir = world_path + '\\' + world_dir.name
    for destination_file in os.scandir(destination_dir):
        # Find destination tags, these include the tag bag references
        if destination_file.name.endswith('.grognok_destination.tft'):
            destination_tag = destination_dir + '\\' + destination_file.name
            with open(destination_tag) as grognok_destination:
                lines_list = grognok_destination.readlines()
                for i in range(len(lines_list)):
                    if lines_list[i].find('FIELD global_tag_bag') >= 0:
                        # Now read the next 4 lines
                        for j in range(4):
                            if lines_list[i + j].find('FIELD m_referenced_tag_name') >= 0:
                                tag_bag_list.append(extract_tag_name(lines_list[i + j]))
                                # There's only one global_tag_bag entry per destination so we should stop here

print(tag_bag_list)
                                
out_file = open('tag_bag_audit.csv','w')
# Find referenced tags from bags in list
for tag_bag in tag_bag_list:
    with open(tag_bag[1]) as f:
        for line in f:
            if line.find('.tft') >= 0:
                tag_name = extract_tag_name(line)
                write_list = [tag_bag[0], tag_name[0], tag_name[1]]
                write_string = (','.join(write_list) + '\n').replace('\\\\', '\\').replace('"', '')
                # What happens when files with the same name are in differently named directories?
                out_file.write(write_string)

# $todo Limit to active Activities
    
# $todo Use extract_tag_name
# Create CSV file for Budget Sets
# Run this from %bungie_project_root%
import os
out_file = open('common_budget_set_audit.csv','w')
path = r'content\common\budget_sets'
# Find all the files in this directory
for budget_set in os.scandir(path):
    budget_set_fullpath = path + '\\' + budget_set.name
    # Now open each file in turn
    with open(budget_set_fullpath) as budget_set_file:
        for line in budget_set_file:
            # If line contains reference to an asset .tft file
            if line.find('.tft') >= 0 and not line.find('budget_source_definition.tft') >= 0:
                tag_name = extract_tag_name(line)
                # Trim out budget_set_file name as well
                budget_set_name = os.path.basename(str(budget_set_file.name))
                budget_set_name = budget_set_name[:budget_set_name.find('.')]
                write_list = [budget_set_name, budget_set_file.name, tag_name[0], tag_name[1]]
                write_string = (','.join(write_list) + '\n').replace('\\\\', '\\').replace('"', '')
                out_file.write(write_string)

end = time.clock()
                
if __name__ == "__main__":
    print('\tFinished!\n\tElapsed time: {:.2f} seconds'.format(end - start))