import json
from wn_client import WNClient

def do(kwargs):
	assert 'url' in kwargs
	assert 'username' in kwargs
	assert 'password' in kwargs
	assert 'obj' in kwargs

	wn = WNClient(kwargs['url'], kwargs['username'], kwargs['password'])

	ret = {}
	if 'extra_kwargs' in kwargs:
		ret.update(kwargs['extra_kwargs'])

	ret.update(kwargs['obj'])

	wn.insert([ret])
