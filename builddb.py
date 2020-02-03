import sqlite3

conn = sqlite3.connect('taskmanager.db')
cur = conn.cursor()

# build a task table
cur.execute("""CREATE TABLE tasks (
                taskid integer primary key autoincrement,
                taskname text,
                desc text, 
                start text, 
                end text, 
                progress integer, 
                completed integer, 
                siteids text, 
                crewids text,
                projids text  
               )""")  # projids was originally projIDs, fix everything else.

# build a sites table
cur.execute("""CREATE TABLE sites (
                siteid integer primary key autoincrement,
                sitename text,
                desc text 
                )""")

# build a crew table
cur.execute("""CREATE TABLE crew (
                crewid integer primary key autoincrement,
                firstname text,
                lastname text, 
                desc text
                )""")


# build a project table
cur.execute("""CREATE TABLE projects (
                projid integer primary key autoincrement,
                projectname text,
                desc text 
                )""")


conn.close()


