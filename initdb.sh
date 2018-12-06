#!/bin/bash

docker exec -it scylla cqlsh -f clean.cql
docker exec -it scylla cqlsh -f init.cql
docker exec -it scylla cqlsh -f populate.cql
