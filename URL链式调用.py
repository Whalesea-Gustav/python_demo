class Chain:
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def user(self, username):
		return Chain('%s/:%s' % (self._path, username))

	def __str__(self):
		return self._path
	__repr__ = __str__


print(Chain().status.users.user('Whalesea').timeline.list)


