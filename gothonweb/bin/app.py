import web
import map

urls = ("/game", "GameEngine", "/", "Index")

app = web.application(urls, globals())

#little hack so that debug mode works with sessions
#
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    
    web.config._session = session
else:
    session = web.config._session
    
render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        #Give us the first session.room = central_corridor
        session.room = map.START
        #Sends you on your way to GameEngine class
        web.seeother("/game")
        
class GameEngine(object):
    #inside the html page you have standard
    def GET(self):
        #session.room should = TRUE, either because it has been through Index, 
	#or been given another link  
        if session.room:
	    #make html page from show_room.html. Take session.room as the 
	    #variable in the html page, accessed by $
	    return render.show_room(room=session.room)
        else:
            # why is there here? do you need it?
            #if something is passed to session.room which is not recognised, it 
	    #won't fail
            return render.you_died()

    def POST(self):
	#inside <form> you can pass method= which takes a function such as GET 
	#or POST(as they are defined in this app)
	#if action is not given a value in the form, it will automatically be 
	#None
	#
        form = web.input(action=None)
        
        if session.room and form.action:
	    #
            session.room = session.room.go(form.action)
            web.seeother("/game")
	#if session.room = laser_weapon_armory and form.action != '123' and 
	 #   count < 10:
		#count =+ 1
		#session.room = session.room.go(form.action)
		#web.seeother("/game")
	    #if session.room = laser_weapon_armory and form.action != '123' and 
		#count >= 10:
		#session.room = None
		#web.seeother("/game")
	    
        else:
	    web.seeother("/game")

if __name__ == "__main__":
    app.run()