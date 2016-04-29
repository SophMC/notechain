import web

#This is mapping /hello to the class index.
#Whenever someone types in /hello they will
#get sent to the index class first. 
urls = (
  '/hello', 'index'
)

'''Whenever /hello is accessed while this app is running, it will begin
   a chain of processes starting from here. /hello is the key for index'''

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class index:
    def GET(self):
	#use render to display a page from the hello_form.html template
	return render.hello_form()
        #name="Nobody is the default if the information is not given
	#inputs=(name="Nobody")
    def POST(self):
	form = web.input(name="Nobody",greet="Hello")
	#forgot to put brackets around form.greet form.name!
	greeting = "%s, %s" % (form.greet, form.name)
	return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()