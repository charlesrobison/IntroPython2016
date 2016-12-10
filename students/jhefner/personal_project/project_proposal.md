<h2>Project: </h2><h3>
Ansible Dynamic Inventory</h3>

This tool's purpose is to interface with the command line tool `ansible`. (https://www.ansible.com/)

This is going to be a tool for myself to use at work and eliminate a _*LARGE*_ amount of manual mysql, grep, awk and other data work.

The python program will need to do the following:

* Connect to a remote mysql server and run select commands.
* Take the return data from mysql select commands and create a specifically useful dictionary of results (if dictionary is the right data model for mysql results).
* Output to stdout json in the format Ansible is expecting in order to properly use the data.

Additional optional things to include (time permitting):
* Make available several command line arguments for input.
* Create useful verbose output to stdout when -v is specified.
