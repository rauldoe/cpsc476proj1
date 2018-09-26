
INSERT INTO users(username, password) VALUES ('pd', 'pd1');
INSERT INTO users(username, password) VALUES ('ed', 'ed1');


INSERT INTO forums(name, creator) VALUES ('first forum', 'pd');
INSERT INTO forums(name, creator) VALUES ('second forum', 'ed');

INSERT INTO threadConversations(forum_id, title, text, author, timestamp) VALUES (1, 'first thread - first forum', 'hey this is great', 'pd', date('now'));
INSERT INTO threadConversations(forum_id, title, text, author, timestamp) VALUES (1, 'second thread - first forum', 'hey this is greatsdddddd', 'pd', date('now'));
INSERT INTO threadConversations(forum_id, title, text, author, timestamp) VALUES (2, 'first thread - second forum', 'hey this is not bad', 'ed', date('now'));
INSERT INTO threadConversations(forum_id, title, text, author, timestamp) VALUES (2, 'second thread - second forum', 'hey this is not basaddddd', 'ed', date('now'));

INSERT INTO posts(thread_id, text, poster, timestamp) VALUES (1, 'post for first thread - first forum', 'pd', date('now'));
INSERT INTO posts(thread_id, text, poster, timestamp) VALUES (1, 'post for second thread - first forum', 'pd', date('now'));
INSERT INTO posts(thread_id, text, poster, timestamp) VALUES (1, 'post for first thread - second forum', 'ed', date('now'));
INSERT INTO posts(thread_id, text, poster, timestamp) VALUES (1, 'post for second thread - second forum', 'ed', date('now'));
