from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None,headers=None, 
status="200"):
    assert status in resp.status, \
    "Expected response %r not in %r" \
    % (status, resp.status)
  
    if status == "200":
	assert resp.data, "Response data is empty."
	
    if contains:
        #confirm that number x, is in resp.data and if now print out.."Response 
        #does not contain...."
	assert contains in resp.data, "Response does not contain %r"\
				      % contains
				    
    if matches:
	reg = re.compile(matches)
	assert reg.matches(resp.data), "Response does not match %r"\
				       % matches
				     
    if headers:
	assert_equal(resp.headers,headers)