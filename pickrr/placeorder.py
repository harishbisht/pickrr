from .session import Session
import requests
import json

class PlaceOrder(object):

	def __init__(self):
		pass


	@staticmethod
	def auth_token():
		return Session.auth_token()


	@staticmethod
	def placeorder(**args):
		try:
			headers = {'content-type': 'application/json'}
			args['auth_token'] = Session.auth_token
			re = requests.post('http://www.pickrr.com/api/place-order/',data= json.dumps(args),headers=headers)
			return re.text
		except Exception,e:
			print e