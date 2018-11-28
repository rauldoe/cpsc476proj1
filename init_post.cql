
DROP TABLE IF EXISTS proj3.posts;
DROP KEYSPACE IF EXISTS proj3;

CREATE KEYSPACE IF NOT EXISTS proj3 
  WITH replication = {'class' : 'SimpleStrategy', 'replication_factor' : 3};

CREATE TABLE IF NOT EXISTS proj3.posts(
  id int PRIMARY KEY, 
  thread_id int, 
  text1 text, 
  poster text,
  timestamp1 timestamp
);
