

CREATE KEYSPACE mykey
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};

USE mykey;

CREATE TABLE posts (
  id uuid PRIMARY KEY,
  thread_id int,
  text1 text,
  poster text,
  timestamp1 timestamp
);

CREATE INDEX idx ON post1s(thread_id);