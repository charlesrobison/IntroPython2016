#!./bin/python

"""
MySQL based Ansible Dynamic Inventory

Objectives defined in the personal_project.md:
* Connect to a remote mysql server and run select commands.
* Take the return data from mysql select commands and create a specifically useful dictionary of results (if dictionary is the right data model for mysql results).
* Output to stdout json in the format Ansible is expecting in order to properly use the data.

Additional optional things to include (time permitting):
* Make available several command line arguments for input.
* Create useful verbose output to stdout when -v is specified.
"""

import sys
import os
import argparse
import pymysql
from configparser import SafeConfigParser
import json

"""
argparse items
"""
parser = argparse.ArgumentParser(description="MySQL based Ansible Dynamic Inventory")
parser.add_argument('--verbose', '-v', action='store_true',
                    help='Verbose output, will break usage if called by ansible')
parser.add_argument('--list', action='store_true', help='list all hosts')
parser.add_argument('--host', action='store', help='list hostvars')
args = parser.parse_args()


#Thought: should i restructure all the below functions and their actions into
# a class? im still a bit confused when a class is more beneficial than
# these functions. im much more comfortable with functions so when thinking
# through this i just kinda relied on functions as i knew how theyd operate.
#
# thinking about it all the actions in these functions share some common elements
# such as the db connection handler etc. it might be a good candidate for a class.

def connect_to_db():
    """
    Create pymysql connection based off of db config file in the same directory.
    """
    parser = SafeConfigParser()
    if os.path.isfile("db.ini"):
        # TODO: is there a better way to read these variables and loop through
        # and set them all at once? maybe have a base config.ini file that
        # tells the program where to read the location of all the other files?
        parser.read("db.ini")
        dbhost = parser.get('db', 'host')
        dbuser = parser.get('db', 'user')
        dbname = parser.get('db', 'db')
        dbpass = parser.get('db', 'pass')
        conn = pymysql.connect(
            host=dbhost, user=dbuser, db=dbname, passwd=dbpass)
    else:
        raise
        #TODO: figure out if a custom exception is needed or if I should be capturing
        # this exception in a specific way. this feels like an opportunity for good
        # error messaging to let the user know that the applications config is incorrect.
    return conn


def query_db(conn):
    """
    take db connection handler and query db based on query within dbquery.ini file in same directory
    """
    c = conn.cursor()
    if args.list:
        parser = SafeConfigParser()
        parser.read("dbquery.ini")
        dbquery = parser.get('query', 'list')
        c.execute(dbquery)
    if args.host:
        parser = SafeConfigParser()
        parser.read("dbquery.ini")
        dbquery = parser.get('query', 'host')
        c.execute(dbquery)
    data = c.fetchall()
    return data

def list_all_machines(conn):
    """
    This whole function bears quite a bit of explanation. The result of this
    function is a dictionary. It is intentional that the `for` loops below create
    a lot of seemingly redundant information in the dict it creates. This is an
    intentional decision to allow Ansible more finite and interesting filtering
    options when it eventually ingests the data.

    The mysql I use looks like:
    select assets.hostname, assets.customer, assets.category, assets.DC_cage, assets.model, assets.make
    from assets

    So 5 columns of data and the results of that query will look something like:
    +----------+----------+----------+---------+----------+------------+
    | hostname | customer | category | DC_cage | model    | make       |
    +----------+----------+----------+---------+----------+------------+
    | server1  | IBM      | Server   |       1 | X1000    | SuperMicro |
    | server2  | BlueBox  | Server   |       1 | Inspiron | Dell       |
    | server3  | IBM      | Server   |       1 | X1000    | SuperMicro |
    | Router1  | BlueBox  | Network  |       1 | SRX240   | Juniper    |
    | Router2  |          | Network  |       1 | SRX550   | Juniper    |
    +----------+----------+----------+---------+----------+------------+

    The `for` loops below go through the data cell by cell and create a dict
    that looks something like:

    {
        "IBM": {
                "hosts": [ "server1,"server3",]
            }
        "Server": {
                "hosts": [ "server1","server2","server3"]
    etc etc etc

    So as you can see the for loops will go through each cell of the mysql results
    and build a list of hostnames who have that same data. So we should end up
    with a dictionary where the keys are all the unique results from the database
    from every column and the "hosts" list should be all the hostnames who match that
    value.

    The output of this dicionary will be json. Due to how the json module works
    it was easist to create the dictionary structure as you saw above so that
    json can take the dict and output a json tree exactly how Ansible is expecting it.

    """

    result = query_db(conn)
    if args.verbose:
        print("Result:", "\n", result, "\n")
        print("Result type: ", type(result))
        print("len(result):", len(result))


    data = {}
    for row in result:
        data[row[1]] = {}  # machines.customer_id
        data[row[2]] = {}  # assets.category
        data[row[3]] = {}  # data_center_cages.name as 'DC_Cage'
        data[row[4]] = {}  # assets.model
        data[row[5]] = {}  # assets.make
        data[row[1]]['hosts'] = []
        data[row[2]]['hosts'] = []
        data[row[3]]['hosts'] = []
        data[row[4]]['hosts'] = []
        data[row[5]]['hosts'] = []
        if args.verbose:
            print("Row:", row)  # row, row your boat

    dictlist = list(data.keys())

    if args.verbose:
        print("\nDict key list:", dictlist)
        print("len(dictlist):", len(dictlist))

    for x in dictlist:
        for row in result:
            if row[1] == x:
                data[row[1]]['hosts'].append(row[0])
            if row[2] == x:
                data[row[2]]['hosts'].append(row[0])
            if row[3] == x:
                data[row[3]]['hosts'].append(row[0])
            if row[4] == x:
                data[row[4]]['hosts'].append(row[0])
            if row[5] == x:
                data[row[5]]['hosts'].append(row[0])
    # _meta is a constructor for Ansible. It is required in the output
    # so I manually created it here and intentionally left its result empty.
    data['_meta'] = {}
    data['_meta']['hostvars'] = {}

    print(data)
    return data


def main():
    conn = connect_to_db()
    if args.list == True:
        bp_dict = list_all_machines(conn)
        print(json.dumps(bp_dict, indent=4, sort_keys=True))
    if args.host:
        sys.exit("--host disabled. Please use --list. This feature will be enabled at a future date.")

if __name__ == '__main__':
    main()