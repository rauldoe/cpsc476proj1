
Note: These are sample calls.  You must adapt them to your installation of Dockers to make it work properly.

Get Container Id
docker ps

Copy Files
docker cp init_post.cql 933e9018f8ea:/init_post.cql

Run CQL script
docker exec -it scylla cqlsh -f init_post.cql

Run CQL query
docker exec -it scylla cqlsh

Run posts initialization
docker exec -it scylla cqlsh -f init_post.cql

Run posts population
docker exec -it scylla cqlsh -f populate_post.cql

