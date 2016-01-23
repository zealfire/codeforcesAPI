import json

class exception:
	def __init__(self):
		''''''

	def unwanted(self, exception):
		exception = json.loads(exception)
		if exception["status"] != "OK":
			return exception["comment"]
		else:
			return "API working fine."