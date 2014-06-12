from random import randint

from lexicon import scan
from sentence import parse_sentence, ParserError

def parse_action(action):
	scanned_words = scan(action)
	print "Scanned words", scanned_words
	return parse_sentence(scanned_words)

class Room(object):

	def __init__(self, name, description, guesses=0):
		self.name = name
		self.error = None
		self.description = description
		self._paths = {}
		self.guesses = guesses

	@property
	def paths(self):
		return self._paths

	@property
	def show_paths(self):
		return '\n'.join(['{} - {}'.format(k, v.name) for k, v in self.paths.items()])
	
	def process_action(self, action, session):
		self.error = None
		try:
			sentence = parse_action(action)
		except ParserError:
			self.error = "Sorry, i didn't understand that."
			return self
		print "Sentence", sentence.subject, sentence.verb, sentence.object_
		if sentence.subject == 'player':
			fn = getattr(self, sentence.verb)
			return fn(sentence.object_, session)
		else:
			raise Exception('NOPE')

	def go(self, direction, session):
		return self.paths.get(direction, None)
		
	def add_paths(self, paths):
	    self._paths.update(paths)

	def shoot(self, object_, session):
		return shoot_death
	
			
class LWA(Room):

	@property
	def paths(self):
		paths = {
			'east' : self._paths['east']
		}
		return paths

	def guess(self, userguess, session):
		
		if session.code != None:
			session.userguess = str(userguess)
			print 'has code in if %r' % (session.code)
			print 'has userguess in if', repr(session.userguess)
			print "guesses", repr(self.guesses)
			self.guesses += 1
			session.drunkenness += 1
			while session.userguess != session.code:
				print "guesses now", self.guesses
				if self.guesses < 10:
					return self
				else:
					return bad_guess_death
			else:
				print 'userguess and code match'
				laser_weapon_armory.add_paths({
												})
				print self.paths
				return the_bridge

		else:
			session.code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
			print "code in else", repr(session.code)
			return laser_weapon_armory

		
			





class BridgeRoom(Room):
	pass

class NameRoom(Room):
	def go(self, name, session):
		session.player.name = name
		print 'NAME {}'.format(session.player.name)
		return hat_room

class HatRoom(Room):
	def go(self, hat, session):
		session.player.hat = hat
		print 'HAT{}'.format(session.player.hat)
		return central_corridor

class ClosetRoom(Room):
	pass


name_room = NameRoom("What's your Name?",
	"Please type your name in the box")

hat_room = HatRoom("What kind of hat would you like?", "Please type the hat in the box")

central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an 
escape pod.

You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body.  He's blocking the door to the
Armory and about to pull a weapon to blast you.
""")

closet_room = ClosetRoom("The Closet",
"""
You're in the closet.  NOT LIKE THAT.  there are some fabulous hats
here, though darling. Type the kind of hat you'd like to wear.  
""")

shoe_room = Room("A Room Of Shoes", 
"""MY GOD.  IT'S FULL OF SHOES.  why don't you pick a pair to wear?
""")

laser_weapon_armory = LWA("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding.  It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container.  There's a keypad lock on the box
and you need the code to get the bomb out.  If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb.  The code is 3 digits.
""")


the_bridge = BridgeRoom("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the
bridge where you must place it in the right spot.

You burst onto the Bridge with the netron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship.  Each of them has an even uglier
clown costume than the last.  They haven't pulled their
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
""")

escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat.
You inch backward to the door, open it, and then carefully
place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button
and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the escape pod to
get off this tin can.

You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes.  It seems like
hardly any Gothons are on the ship, so your run is clear of
interference.  You get to the chamber with the escape pods, and
now need to pick one to take.  Some of them could be damaged
but you don't have time to look.  There's 5 pods, which one
do you take?
""")

the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to
the planet below.  As it flies to the planet, you look
back and see your ship implode then explode like a
bright star, taking out the Gothon ship at the same
time.  You won!
""")

the_end_loser = Room("The End",
"""
You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body
into jam jelly.
"""
)



generic_death = Room("death", "You died in a generic way.")

bomb_death = Room("death", "You throw the bomb, but it bounces back in your face and you die")

shoot_death = Room("death", """
You actually tried to shoot in a spaceship? Fine.  
You try to shoot, but it causes explosive decompression.  
You Died.
""")

bad_guess_death = Room("death", "Man, you just aren't that lucky, are you?  You died.")

escape_pod.add_paths({
	'2': the_end_winner,
	'*': the_end_loser
})

the_bridge.add_paths({
	'throw the bomb': bomb_death,
	'south': laser_weapon_armory,
	'north': escape_pod
})
	

central_corridor.add_paths({
	'south': shoe_room,
	'north': closet_room,
	'west': laser_weapon_armory
})

closet_room.add_paths({
	'south': central_corridor
})

shoe_room.add_paths({
	'north': central_corridor
})


laser_weapon_armory.add_paths({
	'east' : central_corridor
	'north' : the_bridge,
})

START = laser_weapon_armory
