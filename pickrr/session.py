class Session(object):

	auth_token = None

	@staticmethod
	def setup(auth_token):
		Session.auth_token = auth_token

	def __init__(self,auth_token):
		Session.auth_token = auth_token

	@staticmethod
	def showtoken():
	    print Session.auth_token

	@staticmethod
	def auth_token():
	    return Session.auth_token

	@staticmethod
	def clear():
	    Session.auth_token = None
