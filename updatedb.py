import sqlite3

conn = sqlite3.connect('taskmanager.db')

c = conn.cursor()


def update_task_progress(taskid, progress):
    with conn:
        c.execute("UPDATE tasks set progress = :progress where taskid = :taskid",
                  {'taskid': taskid, 'progress': progress})


def update_task_completed( taskid, completed):
    with conn:
        c.execute("UPDATE tasks set completed = :completed where taskid = :taskid",
                  {'taskid': taskid, 'completed': completed})


def update_task_siteid(taskid, siteid):
    with conn:
        c.execute("UPDATE tasks set siteids = :siteids where taskid = :taskid",
                  {'taskid': taskid, 'siteids': siteid})


def update_task_crewid(taskid, crewid):
    with conn:
        c.execute("UPDATE tasks set crewids= :crewid where taskid = :taskid",
                  {'taskid': taskid, 'crewid': crewid})

def update_task_projid(taskid, projid):
    with conn:
        c.execute("UPDATE tasks set projIDs= :projid where taskid = :taskid",  # change projIDs to projids when db is rebuilt.
                  {'taskid': taskid, 'projid': projid})


#print(get_crew_id('Koree'))
#print(get_site_id('yuh'))
#print(get_project_id('PST3'))
#print(get_site_name(2))
#print(get_project_name(1))
#print(get_crew_name(2))
#print(get_task_all())

update_task_progress(1, 90)
update_task_completed(1, 1)
update_task_crewid(1, 2)
update_task_projid(1, 1)
update_task_siteid(1, 2)

