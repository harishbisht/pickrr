class SourceAddress(object):
	is_set = False
	from_name = None
	from_phone_number = None
	from_pincode = None
	from_address = None

	def __init__(self):
		pass

	@staticmethod
	def set(from_name=None,from_address=None,from_pincode=None,from_phone_number=None):
		if len(str(from_pincode)) == 6 and from_name != None and from_address != None and from_phone_number != None:
			SourceAddress.from_name = from_name
			SourceAddress.from_address = from_address
			SourceAddress.from_pincode = from_pincode
			SourceAddress.from_phone_number = from_phone_number
			SourceAddress.is_set = True
		else:
			print "Something went wrong please enter in  format \n SourceAddress.set(from_name<string>,from_address<string>,from_pincode<integer>,from_phone_number<integer>"

