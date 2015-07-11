import datetime

class Member:
	def __init__(self):
		self.memberId = ""
		self.firstName = ""
		self.surname = ""
		self.birthday = ""
		self.age = 0
		self.presentAddress = ""
		self.permanentAddress = ""
		self.mobileNumber_1 = ""
		self.mobileNumber_2 = ""
		self.facebookAddress = ""
		self.cellLeader = ""
		self.invitedBy = ""
		self.firstEventAttended = ""
		self.dateAccepted = ""
		self.pepsolStatus = ""
		self.commitmentLevel = "" #constant, significant, conservative
		self.ninetyDayChallengeLevel = ""
		
	def register(self):
		self.firstName = input("First Name: ")
		self.surname = input("Surname: ")
		self.birthday = input("Birthday: ")
		# self.presentAddress = input("Present Address: ")
		# self.permanentAddress = input("Permanent Address: ")
		# self.mobileNumber_1 = input("Mobile Number: ")
		# self.mobileNumber_2 = input("Backup Mobile Number: ")
		# self.cellLeader = input("Cell Leader: ")
		# self.invitedBy = input("Invited By: ")
		# self.firstEventAttended = input("First Gathering Attended: ")
		# self.dateAccepted = input("Date Accepted: ")
		# self.pepsolStatus = input("PEPSOL Status: ")
		# self.commitmentLevel = input("Commitment Level: ")
		# self.ninetyDayChallengeLevel = input("90-Day Challenge Level: ")
		# self.memberId = "2015-100000"
		
		dateFormat = "%m/%d/%Y"
		dateObject = datetime.datetime.strptime(self.birthday, dateFormat)
		# self.age = (datetime.date.today() - dateObject) 
		print("Date Today: " + str(datetime.date.today()))
		print("DateObject: " + str(dateObject))
		print("Age: ")