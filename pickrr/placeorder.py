from .session import Session

class PlaceOrder(object):

	def __init__(self):
		pass


	@staticmethod
	def auth_token():
	    return Session.auth_token()
