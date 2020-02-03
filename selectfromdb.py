import sqlite3

conn = sqlite3.connect('taskmanager.db')

c = conn.cursor()

def get_task_all():
    with conn:
        c.execute("SELECT * FROM tasks")
        return c.fetchall()
def get_crew_name(id):
    with conn:
        c.execute("SELECT firstname FROM crew where crewid = :id ", {'id': id})
        return c.fetchone()

def get_site_name(id):
    with conn:
        c.execute("SELECT sitename FROM sites where siteid = :id", {'id': id})
        return c.fetchone()


def get_project_name(id):
    with conn:
        c.execute("SELECT projectname FROM projects where projID= :id", {'id': id})  # change projID to projid when db is rebuilt.
        return c.fetchone()

def get_crew_id(name):
    with conn:
        c.execute("SELECT crewid FROM crew where firstname = :name ", {'name': name})
        return c.fetchone()

def get_site_id(name):
    with conn:
        c.execute("SELECT siteid FROM sites where sitename = :name", {'name': name})
        return c.fetchone()


def get_project_id(name):
    with conn:
        c.execute("SELECT projID FROM projects where projectname= :name", {'name': name})
        return c.fetchone()

def close_db():
    conn.close()

print(get_crew_id('Koree'))
print(get_site_id('yuh'))
print(get_project_id('PST3'))
print(get_site_name(2))
print(get_project_name(1))
print(get_crew_name(2))
print(get_task_all())


#print('From Crew:', c.fetchall())
#print()
#c.execute("SELECT sitename FROM sites")
#print('From Sites: ', c.fetchall())
#print()
#c.execute("SELECT projectname FROM projects")
#print('From Projects: ', c.fetchall())
#c.execute("SELECT taskname, desc, start, end, progress  FROM tasks")
#print('From Tasks: ', c.fetchone())
#c.execute("SELECT taskid, taskname, desc, siteIDs, crewIDs, projIDs FROM tasks WHERE taskid = 1")
#print('From Task, select taskid 1: ', c.fetchone())

close_db()
#conn.close()
