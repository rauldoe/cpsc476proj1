
Note: These are sample calls.  You must adapt them to your installation of Dockers to make it work properly.

Run Python tester to test your Scylla setup
clear; python test_cql.py
clear; python3 test_cql.py

Get IP Address of Container, 172.17.0.2
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' scylla

Get Container Id
docker ps

Copy Files
docker cp init_post.cql scylla:/init_post.cql
docker cp populate_post.cql scylla:/populate_post.cql

Run CQL script
docker exec -it scylla cqlsh -f init_post.cql
docker exec -it scylla cqlsh -f populate_post.cql

Run CQL query
docker exec -it scylla cqlsh

Run posts initialization
docker exec -it scylla cqlsh -f init_post.cql

Run posts population
docker exec -it scylla cqlsh -f populate_post.cql

