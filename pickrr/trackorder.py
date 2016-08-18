from .session import Session
import requests
import json

class TrackOrder(object):

	def __init__(self,**args):
		pass

	@staticmethod
	def trackorder(**args):
		try:
			headers = {'content-type': 'application/json'}
			url ="http://www.pickrr.com/api/tracking-json/?tracking_id=" + str(args['tracking_id'])
			re = requests.get(url,headers=headers)
			return re.text
		except Exception,e:
			print e