
from dbhelper import dbhelper
from populate_post import populate_post

# dbhelper.executeScriptPath("proj1.db", "init.sql")
# dbhelper.executeScriptPath("proj1.db", "populate.sql")

dbhelper.executeScriptPath("post0.db", "init_post.sql")
dbhelper.executeScriptPath("post1.db", "init_post.sql")
dbhelper.executeScriptPath("post2.db", "init_post.sql")

populate_post.process()
