from nose.tools import *
#How to import an application and run it directly for the automated test! 
#Important!
from bin.app import app
#From dir tests, import assert_response function from tools.py
from tests.tools import assert_response

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp,status="404")
    
    #test our first GET request to /hello
    resp = app.request("/game")
    assert_response(resp)
    
    #make sure default values work for the form
    #resp = app.request("/game", method="POST")
    #assert_response(resp, action=None)
    
    # test that we get expected values
    #data = {'name':'Zed','greet':'Hola'}
    #resp = app.request("/hello", method="POST",data=data)
    #assert_response(resp,contains="Zed")