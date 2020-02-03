#This is just a starting idea for a class object that will hold information 
#of each task.
I have a new setup. 
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
