import json
from wn_client import WNClient

def do(kwargs):
	assert 'url' in kwargs
	assert 'username' in kwargs
	assert 'password' in kwargs
	assert 'obj' in kwargs

	wn = WNClient(kwargs['url'], kwargs['username'], kwargs['password'])

	wn.insert(kwargs['obj'])
