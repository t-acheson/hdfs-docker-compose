# Docker HDFS Setup

### Note
Idek what the resourcemanager and the nodemanager are doing right now, but the namenode and datanode are doing bits

## Running
1. Make sure to specify 

`docker compose up --build --force-recreate`

because I have run into issues with incompatible ClusterIds and datanode failures because of it.

I presume it has something to do with the way Docker caches stuff. 

One it's running you can check check out the dashboard here: http://localhost:9870/dfshealth.html#tab-overview

2. To set the necessary folders and write permissions (`write.py` will fail otherwise), run: 

`bash init-dhfs.sh`

3. Sort your Python environment ya' filthy animal

`venv && source .venv/bin/activate && pip install -r requirements.txt`

4. To write the test data the run:
`python write.py`

5. And finally to read it, run:
`python read.py`

Congratulations! You have just created a distributed file system, written a file to it, and read it again. Pat on the back.

## N.B.
The host specified in `/config/hdfs-site.xml` is currently: *hdfs://namenode:9000*; as in *namenode* the name of the the Docker service in the compose file.

You will likely run into problem if you try to run the namenode on it's own.

### This setup is designed to be run as a compose for now

## Docker Volumes
Because many nodes need access to the same config those are saved as a volume at `/config`, editing those will edit the config for the entire cluster (all of the clusters I suppose, considering each container is supposedly its own cluster)

## Resiliency
Have a little fun, run:

`docker stop cc_med-datanode1-1`

I've set the heartbeat timeouts to be super short, see `/config/hdfs-site.xml`

If you're looking at your Docker output, the namenode will say it's removing one of the nodes from the rack

And you can see the status of the nodes here http://localhost:9870/dfshealth.html#tab-datanode