def loadFileContents(filename):
	recordList = []
	with open(filename) as inputFile:
		for line in inputFile:
			recordList.append(line)
	return recordList
	
class HarvestEvent:
	def __init__(self):
		self.eventId = ""
		self.eventType = ""
		self.eventMarker = "01" #for many sessions such as Sunday Service, defaults to 01 for events such as Youth Camp
		self.eventName = ""
		self.speaker = ""
		self.topic = ""
		self.dateStarted = ""
		self.dateEnded = ""
		self.timeStarted = ""
		self.timeEnded = ""
		self.location = ""
		self.notes = ""
		
	def create(self):
		self.eventType = input("Harvest Event Type: ")
		self.eventMarker = input("Harvest Event Marker: ")
		self.eventName = input("Harvest Event Name: ")
		self.speaker = input("Speaker: ")
		self.topic = input("Topic: ")
		self.dateStarted = input("Date Started: ")
		self.dateEnded = input("Date Ended: ")
		self.timeStarted = input("Time Started: ")
		self.timeEnded = input("Time Ended: ")
		self.location = input("Location: ")
		self.notes = input("Notes: ")
		self.eventId = self.eventType + "-" + self.dateStarted.replace('/', '') + "-" + self.eventMarker
		print("Created event! Harvest Event Id is " + self.eventId)
		return self.serialize(self)
		
	def serialize(self, event):
		return event.eventId + ";" + \
			event.eventType + ";" + \
			event.eventMarker + ";" + \
			event.eventName + ";" + \
			event.speaker + ";" + \
			event.topic + ";" + \
			event.dateStarted + ";" + \
			event.dateEnded + ";" + \
			event.timeStarted + ";" + \
			event.timeEnded + ";" + \
			event.location + ";" + \
			event.notes
			

class EventHandler:
	def __init__(self):
		self.harvestEventsFilePathAndName = "textFiles/harvestEvents.txt"
	
	def createNewEvent(self):
		event = HarvestEvent()
		serializedEvent = event.create()
		self.saveToFile(serializedEvent)
		
	def saveToFile(self, eventDetails):
		teamEvents = open(self.harvestEventsFilePathAndName, "a")
		teamEvents.write(eventDetails + "\n")
		teamEvents.close()
		print("New event saved!")

	def getGridOfEvents(self):
		grid = []
		index = -1
		records = loadFileContents(self.harvestEventsFilePathAndName)
		for record in records:
			index += 1
			grid.append([])
			fields = record.split(';')
			for field in fields:
				grid[index].append(field)
		
		return grid