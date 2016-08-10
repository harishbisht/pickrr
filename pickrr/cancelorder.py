from .session import Session
import requests
import json

class CancelOrder(object):

	def __init__(self,**args):
		pass

	@staticmethod
	def cancelorder(**args):
		try:
			headers = {'content-type': 'application/json'}
			args['auth_token'] = Session.auth_token
			re = requests.post('http://www.pickrr.com/api/order-cancellation/',data= json.dumps(args),headers=headers)
			return re.text
		except Exception,e:
			print e