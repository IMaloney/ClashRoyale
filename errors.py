
class Error(Exception):
	pass 

class IncorrectParamtersError(Error):
	def __init__(self):
		self.message = "Client provided incorrect parameters for the request."

class AccessDeniedError(Error):
	def __init__(self):
		self.message = "Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource."

class ResourceError(Error):
	def __init__(self):
		self.message = "Resource not found."

class UnknownError(Error):
	def __init__(self):
		self.message = "Unknown error when handling the request."

class ServiceError(Error):
	def __init__():
		self.message = "Service temporarily unavailable due to maintanence."

class ServerError(Error):
	def __init__():
		self.message = "Could not connect to server."


def handle_error(error: str) -> None:
	if error == "accessDenied":
		raise AccessDeniedError()
	if error == "notFound":
		raise ResourceError()