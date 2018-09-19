
INSERT INTO users(username, password) VALUES ('pd', 'pd1');
INSERT INTO users(username, password) VALUES ('ed', 'ed1');


INSERT INTO forums(name, creator) VALUES ('first forum', 'cd343');
INSERT INTO forums(name, creator) VALUES ('second forum', 'md2323');

INSERT INTO threads(forum_id, title, text, author, timestamp) VALUES (1, 'first title', 'hey this is great', 'paul', date('now'));
INSERT INTO threads(forum_id, title, text, author, timestamp) VALUES (2, 'second title', 'hey this is not bad', 'steve', date('now'));
