DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  thread_id INTEGER NOT NULL,
  text VARCHAR(1000) NOT NULL,
  poster VARCHAR(250) NOT NULL,
  timestamp DATETIME NOT NULL,
  FOREIGN KEY (thread_id) REFERENCES threadConversations (id),
  FOREIGN KEY (poster) REFERENCES users (username)
);
