import sqlite3

conn = '' #sqlite3.connect('taskmanager.db')

#c = conn.cursor()

#cur.execute("""CREATE TABLE crew (
#                id integer,
#                firstname text,
#                lastname text,
#                desc text
#                )""")
if conn :
    print('conn is up')
else:
    print('conn is down')

def insert_crew(first, last, desc):
    with conn:
        c.execute("""INSERT INTO crew (firstname, lastname, desc) 
                    VALUES (:first, :last, :desc )""",
                    {'first': first, 'last': last, 'desc': desc})


def insert_projects(projectname, desc):
    with conn:
        c.execute("INSERT INTO projects (projectname, desc) \
                    VALUES (:projectname, :desc )",
                    {'projectname': projectname, 'desc': desc})


def insert_tasks(taskname, desc, start, end):
    with conn:
        c.execute("""INSERT INTO tasks (taskname, desc, start, end)
                    VALUES (:taskname, :desc, :start, :end)""",
                    {'taskname': taskname, 'desc': desc, 'start': start, 'end': end})


def insert_sites(sitename, desc):
    with conn:
        c.execute("""INSERT INTO sites (sitename, desc) 
                    VALUES (:sitename, :desc )""",
                    {'sitename': sitename, 'desc': desc})


#insert_crew('Jenna', 'mac', 'works in ead')
#insert_crew('James', 'Cole', 'works in lab2')
#insert_crew('Koree', 'Garrett', 'works in lab2')
#insert_crew('Chris', 'Knight', 'contractor')
#insert_projects('PST3', 'located at PST3')
#insert_projects('STM2', 'localed in st')
#insert_projects('YUM2', 'local space')
#insert_sites('pyu2', 'none')
#insert_sites('yuh', 'none')
#insert_sites('thu', 'none')
#insert_tasks('Cab cleanup', 'clean up the cab returns', '2020-02-12', '2020-02-14')





#c.execute("SELECT * FROM crew")
#print(c.fetchall())

#conn.close()