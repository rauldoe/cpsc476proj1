
INSERT INTO users(username, password) VALUES ('pd', 'pd1');
INSERT INTO users(username, password) VALUES ('ed', 'ed1');


INSERT INTO forums(name, creator) VALUES ('first forum', 'cd343');
INSERT INTO forums(name, creator) VALUES ('second forum', 'md2323');

INSERT INTO threadConversations(forum_id, title, text, author, timestamp) VALUES (1, 'first thread - first forum', 'hey this is great', 'paul', date('now'));
INSERT INTO threadConversations(forum_id, title, text, author, timestamp) VALUES (1, 'second thread - first forum', 'hey this is greatsdddddd', 'paul schloe', date('now'));
INSERT INTO threadConversations(forum_id, title, text, author, timestamp) VALUES (2, 'first thread - second forum', 'hey this is not bad', 'steve', date('now'));
INSERT INTO threadConversations(forum_id, title, text, author, timestamp) VALUES (2, 'second thread - second forum', 'hey this is not basaddddd', 'steveiebe', date('now'));

INSERT INTO posts(thread_id, text, poster, timestamp) VALUES (1, 'post for first thread - first forum', 'paudkddl', date('now'));
INSERT INTO posts(thread_id, text, poster, timestamp) VALUES (1, 'post for second thread - first forum', 'jack', date('now'));
INSERT INTO posts(thread_id, text, poster, timestamp) VALUES (1, 'post for first thread - second forum', 'ames', date('now'));
INSERT INTO posts(thread_id, text, poster, timestamp) VALUES (1, 'post for second thread - second forum', 'ines', date('now'));
