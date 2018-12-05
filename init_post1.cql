

DROP TABLE IF EXISTS proj3.post1s;
DROP KEYSPACE IF EXISTS proj3;

CREATE KEYSPACE IF NOT EXISTS proj3 
  WITH replication = {'class' : 'SimpleStrategy', 'replication_factor' : 3};

USE proj3;

CREATE TABLE IF NOT EXISTS post1s(
  id int PRIMARY KEY, 
  thread_id int, 
  text1 text, 
  poster text,
  timestamp1 timestamp
);
