import sqlite3


	
class Taskdb(self):
	database = 'taskmanager.db'
	# get all of the variables.
	def __init__(self, createdate, titleofproject, startdate, enddate):  # change this before running.
		self.createdate = createdate
		self.titleofproject = titleofproject
		self.startdate = startdate
		self.enddate = enddate
        
	
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
	def close_db():
		conn.close()
	def open.db():
		conn = sqlite3.connect(self.database)
		
  
