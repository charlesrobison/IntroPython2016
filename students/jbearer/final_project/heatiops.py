#!/usr/bin/env/python3

import os
import subprocess

dict_path_iops = {}
dict_node_iops = {}
dict_total_iops = {}

file_list = []

def check_queues():

    quePaths = ['/Users/jbearer/scripts/misc/clus1/queued/', 
                '/Users/jbearer/scripts/misc/clus2/queued/']

    for paths in quePaths:
        fileName = os.listdir(paths)
        for file in fileName:
            file_list.append(paths + file)

    # print('file_list:', file_list)


def proc_file():

    for parse_file in file_list:
        path_file = os.path.split(parse_file)
        fileName = path_file[1]
        clusterName = path_file[1]
        clusterName = clusterName.split('_')
        clusterName = clusterName[0]

        with open(parse_file, 'r') as file_in:
            for line in file_in:
                heat_line = line.strip('\n').split(',')
                if heat_line != ['']:
                    proc_lines(heat_line, parse_file)
        write_db_file(clusterName, parse_file)
        parkPath = parse_file.replace('queued', 'parked')
        os.rename(parse_file, parkPath)
        dict_path_iops.clear()
        dict_node_iops.clear()
        dict_total_iops.clear()


def proc_lines(heat_line, parse_file):

    global myDate #Are declaring global variables BAD? If so, why? What is another way?

    newPath = []

    try:
        myDate = heat_line[0]
        myEventOps = float(heat_line[1])
        myNode = heat_line[2]
        myEvent = heat_line[3]
        myPath = str(heat_line[6]).split('/')

        if myPath[0] == '' or myPath[0] == '"':
            del myPath[0]

        if len(myPath) > 4 and myPath[2] == 'share':
            for i in range(4):
                newPath.append(myPath[i])
        elif len(myPath) >= 3:
            for i in range(3):
                newPath.append(myPath[i])
        else:
            for i in range(len(myPath)):
                newPath.append(myPath[i])

        newPath = '_'.join(newPath)

        if newPath not in dict_path_iops:
            dict_path_iops[newPath] = {myEvent: myEventOps}
        elif myEvent not in dict_path_iops[newPath]:
            dict_path_iops[newPath].update({myEvent: myEventOps})
        else:
            add_ops = dict_path_iops[newPath][myEvent] + myEventOps
            add_ops = round(add_ops, 2)
            dict_path_iops[newPath][myEvent] = add_ops

        if myNode not in dict_node_iops:
            dict_node_iops[myNode] = myEventOps
        else:
            add_ops = dict_node_iops[myNode] + myEventOps
            add_ops = round(add_ops, 2)
            dict_node_iops[myNode] = add_ops

        if 'total_iops' not in dict_total_iops:
            dict_total_iops['total_iops'] = myEventOps
        else:
            dict_total_iops['total_iops'] = dict_total_iops['total_iops'] + myEventOps

    except IndexError:
        errPath = parse_file.replace('queued', 'errors')
        os.rename(parse_file, errPath)
        raise


def write_db_file(clusterName, parse_file):

    out_file_name = clusterName + '_' + str(myDate) + '.txt'
    procPath = os.path.split(parse_file)
    procPath = procPath[0].replace('queued', 'processed')
    procPath = os.path.join(procPath, out_file_name)

    # InfluxDB requires the epoch time to be in nanoseconds.
    epochDate = int(myDate) * 1000000000

    with open(procPath, 'w') as out:

        for myPath, values in dict_path_iops.items():
            for myEvent, myEventOps in values.items():
                out.write('heatiops,clustername={},path={},event={} ops={} {}\n'.format(clusterName,
                myPath, myEvent, myEventOps, epochDate))

        for myNode, myEventOps in dict_node_iops.items():
            out.write('heatiops,clustername={},node={} ops={} {}\n'.format(clusterName,
                myNode, myEventOps, epochDate))

        for total_iops, totalOps in dict_total_iops.items():
            out.write('heatiops,clustername={} ops={} {}\n'.format(clusterName, 
                round(totalOps, 2), epochDate))

    url = 'http://localhost:8086/write?db=heatiops'
    subprocess.call(['curl', '-i', '-XPOST', url, '--data-binary', '@' + procPath])


if __name__ == '__main__':
    check_queues()

    if file_list:
        proc_file()

