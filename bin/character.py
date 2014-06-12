class Person(object):
	def __init__(self, name):
		self.name = name


class Player(Person):
	def __init__(self, hat, *args):
		super(Player, self).__init__( *args)
		self.hat = hat


PLAYER = Player('Fedora', 'Steve McNeckbeard')