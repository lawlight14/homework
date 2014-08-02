class Member(object):
	def __init__(self):
		self.id = ""
		self.pw = ""
	def set(self, user_id, user_pw):
		self.id = user_id
		self.pw = user_pw
	def get_id(self):
		return self.id
	def get_pw(self):
		return self.pw