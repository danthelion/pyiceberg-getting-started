#!/bin/bash

start-master.sh -p 7077
start-worker.sh spark://spark-iceberg:7077
start-history-server.sh
start-thriftserver.sh

spark-submit /home/iceberg/scripts/load_data.py
