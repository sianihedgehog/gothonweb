import web

import character

urls = (
	'/game', 'GameEngine',
	'/', 'Index',
)

app = web.application(urls, globals())

#little hack so debug works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store,
									initializer={'room': None, 'drunkenness': 0, 'player': None,
									 'hat':'fedora', 'userguess': 0, 'code': None})
	# session = web.session.Session(app, store,
	# 								initializer={'room': None, 'drunkenness': 0, 'player': None,
	# 								 'hat':'fedora', 'code': 0, 'guesses': 0})
	web.config._session = session
else:
	session = web.config._session
import map

render = web.template.render('templates/', base="layout")

class Index(object):
	def GET(self):
		print 'getting from Index'
		# this is used to "setup" the session with starting values
		session.room = map.START
		session.player = character.PLAYER
		# session.drunkenness = 0
		web.seeother("/game")
		
class GameEngine(object):
	
	def GET(self):
		print '{} has a {} hat, and is {} drunk.  userguess is {} and code is {}'.format(
			session.player.name,
			session.player.hat,
			session.drunkenness,
			session.userguess,
			session.code
		)
		if session.room:
			return render.show_room(room=session.room)
		else:
			# why is this here, do you need it?
			return render.you_died()
			
	def POST(self):
		form = web.input(action=None)
		# there is a bug here, can you fix it?
		if session.room and form.action:
			session.room = session.room.process_action(form.action, session)
		else:
			session.room
		# maybe lack of else statement? SE
		web.seeother("/game")
		
if __name__ == "__main__":
	app.run()