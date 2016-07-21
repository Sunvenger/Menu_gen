class menu :
	items_=[]
	def __init__(self,*items):
		self.items_=items
	def __str__(self):
		str_=""
		for item in self.items_:
			str_+="%r\n"%item
		return str_
	
	
