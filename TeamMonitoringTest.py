import EventModule
import MemberModule

class MasterListHandler:
	def __init__(self):
		print("")
		
	def addNewMember(self):
		member = MemberModule.Member()
		serializedMemberDetails = member.register()
		print("New member added!")
		

class AttendanceList:
	def __init__(self):
		print("")

class TeamMonitoring:
	def __init__(self):
		self.masterListHandler = MasterListHandler()
		self.eventHandler = EventModule.EventHandler()
		self.attendanceList = AttendanceList()
		print ("Team Monitoring Class created!")
		
	def execute(self):
		self.displayMenu();
		response = input("Enter choice: ")
		while (not ( (response >= 'A' and response <= 'G') or (response >= 'a' and response <= 'g')) ):
			response = input("Invalid key!\nEnter choice: ")
		self.processChoice(response.lower())
		
	def displayMenu(self):
		print("What do you wish to do? ", \
		"\n\t[A] Create New Harvest Event", \
		"\n\t[B] View Harvest Event List", \
		# "\n\t[B2] Edit Harvest Event", \
		# "\n\t[B3] Delete Harvest Event", \
		"\n\t[C] Add New Member", \
		"\n\t[D] Edit Master List of Members", \
		"\n\t[E] Create New Attendance Sheet", \
		"\n\t[F] Update Attendance Sheet", \
		"\n\t[G] Exit")
		# [B] which event?
		# [D] show master list
		# [E] for which event?
		# [F] which sheet?
		
	def processChoice(self, userResponse):
		if userResponse == 'a':
			self.eventHandler.createNewEvent()
		elif userResponse == 'b':
			grid = self.eventHandler.getGridOfEvents()
			self.displayGrid(grid)
		elif userResponse == 'c':
			self.masterListHandler.addNewMember()
		elif userResponse == 'd':
			print("Response: D")
		elif userResponse == 'e':
			print("Response: E")
		elif userResponse == 'f':
			print("Response: F")
		elif userResponse == 'g':
			print("Response: G")
		else:
			print("should assert!")
	
	def displayGrid(self, grid):
		for record in grid:
			for field in record:
				print(field)

tm = TeamMonitoring()
tm.execute()