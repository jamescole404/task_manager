'''
what will this program do?
- track tasks inside the vlab.
- These tasks will be assigned to one or more people. 
- There is a start date and an 
- end date for each task. 
- The tasks can be assigned to 
    - a site number or 
    - a project number.
- These tasks will be grouped in a list shown on a screen. 
    - The groups can be 
        - person, 
        - site, or 
        - project. 
- The screen will have several displays that show in sequence.
    - The displays are: need time for each to stay on screen.
        - weekly goals/tasks, 
        - monthly goals/tasks, 
        - yearly goals/tasks 
        - daily goals/tasks list. The daily one should be the main displays.
- info needed for program, so far
    - Task Name
    - Start date/time
    - End date/time
    - progress in %
    - name or names assigned to task
    - task description
  
- an idea occured to me. why not add a work time list for each person.
    that way tasks can be assigned by time as well. 
    
I don't want to take the place of a calendar. I want this to be 
only for availible tasks that need to be assigned and when they need to get
done. 


basic layout:
#############################################################################
############################# DAY TASKING ###################################
#############################################################################
#| Task Name | Start |  End  | progress (%) | Name(s) Assigned | Task Desc |# | site |
#|           |       |       |              |                  |           |#
#############################################################################

#############################################################################
############################ WEEK TASKING ###################################
#############################################################################
#| Task Name | Start |  End  | progress (%) | Name(s) Assigned | Task Desc |#
#|           |       |       |              |                  |           |#
#############################################################################

#############################################################################
########################### MONTH TASKING ###################################
#############################################################################
#| Task Name | Start |  End  | progress (%) | Name(s) Assigned | Task Desc |#
#|           |       |       |              |                  |           |#
#############################################################################



This will be in a program window on a raspberry pi, full screen. 

'''
'''
Database set up ideas
tables
    crew - this will hold all of the people that can be assigned to a task. 
        namefirst, namelast, (key)IDnum,  
    task - this holds the task info
        title, desc, (key)IDnum, dateCreated, dateStart, dateEnd, taskProgress
    projects - um... projects are listed here, this can be links or other stuff.
        (key)IDnum, projectname 
    sites - encrypetd site list 
        (key)IDnum, sitename   

'''
'''
Based on the tables, need to be able to 
    - add/del/update for all tables
    - pull data from tables 
'''
'''

files setup 
    task.py - Task() class file. holds all of the variables before saving to table.
    tasktracker.py - main() file. 
        

'''



####### IGNORE BELOW #######
#This is just a starting idea for a class object that will hold information 
#of each task.
class Task_Tracker(self, createdate, titleofproject, startdate, enddate):
	createdate = 0 # int
	titleofproject = '' # str
	startdate = 0 # int
	enddate = 0 # int
	peopleassigned = [] # list
	description = '' # str

	def __init__(self, createdate, titleofproject, startdate, enddate):
		self.createdate = createdate
        self.titleofproject = titleofproject
        self.startdate = startdate
        self.enddate = enddate
        
	
	def assignPeople(self, peopleassigned): # use a list object
        self.peopleassigned = peopleassigned
       
    def changeEnddate(self, newdate):
        self.enddate = newdate
        
    def changeStartdate(self, newdate):
        self.startdate = newdate
   
    def addDescription(self, descrip)
        self.description = descrip
        
    


