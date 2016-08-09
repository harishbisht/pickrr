from .session import Session

class PlaceOrder(object):

	auth_token = None

	def __init__(self,auth_token):
		Session.auth_token = auth_token

	@staticmethod
	def showtoken():
	    print Session.auth_token

	@staticmethod
	def auth_token():
	    return Session.auth_token
