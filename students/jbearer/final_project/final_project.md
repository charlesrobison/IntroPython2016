
# Process Heat Statistics
---

Description:

This program will process heat data created by Isilon clustererd storage.  The data 
being parsed will be presented in a comma separated file.  Data will be coming in 
from multiple clusters.  The following is a list of functions that the program
will need to do:

1. Periodically check a queue directory where the cluster will place the generated
    on an hourly basis.

2. If the queue folders have data present, a list will be created to tell the
    program the paths and files that need to be processed.

3. The files processed will be be compiling IOPS for paths, nodes and the
    total for the cluster.

4. After the file has been processed it will be moved to a parked directory.

5. The processed data will be written in a file format that can be input into an
    InfluxDB database and written to a processed directory.

6. An error directory will exist should there be a file generated that the
    program cannot process.
