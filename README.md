#Yahoo! Cloud System Benchmark (YCSB)

This version of the YCSB tool adds adds support for Aerospike 3 to the Thumbtack Technology version that was originally modified to to add support for Aerospike and Couchbase databases, to improve MongoDB driver and to add some automation to run YCSB on multiple clients.


##Links
http://wiki.github.com/brianfrankcooper/YCSB/
https://github.com/couchbaselabs/YCSB
http://research.yahoo.com/Web_Information_Management/YCSB
https://fabric.readthedocs.org/en/1.3.2/


##Step by step

1. Download the latest release of YCSB:

```bash
    git clone https://github.com/aerospike/ycsb
    cd ycsb
```
2. Set up a database and client hosts to benchmark. 
   There is a README file under each binding directory.
   
   You must have SSH (and in most cases root) access to all your hosts.

3. Configure YCSB build script to build database binders
   Edit pom.xml, uncomment modules related to databases which you chose in `<modules>` section

4. Configure hosts, databases and workloads settings:
   Edit files: conf/hosts.py, conf/databases.py, conf/workloads.py

5. Build and deploy YCSB to client hosts
```bash
    fab ycsb_deploy
```
6. Load data to databases
```bash
    fab ycsb_load:db=<dbname>
```
   `<dbname>` is aerospike, couchbase, couchbase2, cassandra, 
   mongodb or any other you configured
   Edit conf/workloads.py to confiture workloads root directory

7. Run YCSB workload
```bash
    fab ycsb_run:db=<dbname>,workload=A
```
8. Check the YCSB status
```bash 
    fab ycsb_status:db=<dbname>
```
9. Download YCSB results and logs
```bash
    fab ycsb_get:db=<dbname>,do=True
```    
   You'll get some .out and .err files in the current directory downloaded
   from all your clients.

10. Aggregate the YCSB results
```bash
    ./bin/merge.py
```    
   This script gets the most important parameters from YCSB .out files,
   such as throughput and latency, aggregates the results from multiple clients
   and prints the result as tab-separated values which can be easy pasted
   into any spreadsheet.

##Notes

This tool was tested using following software versions
* Ubuntu Server (12.04)
* Git (1.7.10.4)
* openjdk-7-jdk (7u9-2.3.3)
* Maven (2.2.1)
* Fabric (1.3.2)
* Python (2.7.3)